#!/usr/bin/env python3
import logging
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
DATA_DIR = Path("data")
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def safe_building_name_from_filename(path: Path) -> str:
    stem = path.stem
    parts = stem.split("_")
    if len(parts) >= 2 and parts[1].strip():
        return parts[1].upper()
    return stem.upper()

def ingest_and_validate_data() -> pd.DataFrame:
    logging.info("Starting ingestion.")
    frames = []
    if not DATA_DIR.is_dir():
        logging.error("Data directory not found at %s", DATA_DIR)
        return pd.DataFrame()
    csv_files = sorted(DATA_DIR.glob("*.csv"))
    if not csv_files:
        logging.warning("No CSV files found in %s", DATA_DIR)
        return pd.DataFrame()
    for file_path in csv_files:
        try:
            df = pd.read_csv(file_path, on_bad_lines="skip", low_memory=False)
            if df.shape[1] < 1:
                logging.warning("Skipping %s — no columns", file_path.name)
                continue
            cols = [c.strip() for c in df.columns]
            timestamp_col = None
            kwh_col = None
            for c in cols:
                lc = c.lower()
                if 'time' in lc or 'date' in lc:
                    timestamp_col = c
                if lc in ('kwh', 'kw', 'energy', 'value'):
                    kwh_col = c
            if timestamp_col is None:
                timestamp_col = cols[0]
            if kwh_col is None:
                if len(cols) > 1:
                    kwh_col = cols[1]
                else:
                    logging.warning("Skipping %s — no plausible kwh column", file_path.name)
                    continue
            df = df[[timestamp_col, kwh_col]].rename(columns={timestamp_col: "Timestamp", kwh_col: "kwh"})
            df["Building"] = safe_building_name_from_filename(file_path)
            df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
            df["kwh"] = pd.to_numeric(df["kwh"], errors="coerce")
            df = df.dropna(subset=["Timestamp", "kwh"])
            frames.append(df)
            logging.info("Ingested %d rows from %s", len(df), file_path.name)
        except Exception as exc:
            logging.exception("Failed to ingest %s: %s", file_path.name, exc)
    if not frames:
        logging.warning("No valid data ingested.")
        return pd.DataFrame()
    combined = pd.concat(frames, ignore_index=True)
    combined = combined.sort_values("Timestamp").set_index("Timestamp")
    logging.info("Combined dataframe has %d rows", len(combined))
    return combined

def calculate_daily_totals(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame(columns=["Timestamp", "Building", "Daily_kwh_Total"])
    daily = df.groupby("Building")["kwh"].resample("D").sum()
    daily = daily.reset_index().rename(columns={"kwh": "Daily_kwh_Total"})
    return daily

def calculate_weekly_aggregates(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame(columns=["Timestamp", "Building", "Weekly_kwh_Total"])
    weekly = df.groupby("Building")["kwh"].resample("W").sum()
    weekly = weekly.reset_index().rename(columns={"kwh": "Weekly_kwh_Total"})
    return weekly

def building_wise_summary(df: pd.DataFrame):
    if df.empty:
        return pd.DataFrame(columns=["Building", "Mean_kwh", "Min_kwh", "Max_kwh", "Total_kwh"]), {}
    summary_df = df.groupby("Building")["kwh"].agg(
        Mean_kwh="mean",
        Min_kwh="min",
        Max_kwh="max",
        Total_kwh="sum"
    ).reset_index()
    summary_dict = summary_df.set_index("Building").T.to_dict("dict")
    return summary_df, summary_dict

class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = pd.to_datetime(timestamp)
        self.kwh = float(kwh)

class Building:
    def __init__(self, name: str):
        self.name = name
        self.meter_readings = []
    def add_reading(self, timestamp, kwh):
        try:
            r = MeterReading(timestamp, kwh)
            self.meter_readings.append(r)
        except Exception:
            pass
    def calculate_total_consumption(self) -> float:
        return sum(r.kwh for r in self.meter_readings)
    def generate_report(self) -> str:
        total = self.calculate_total_consumption()
        return f"--- Report for Building {self.name} ---\nTotal Consumption: {total:,.2f} kWh\n"

class BuildingManager:
    def __init__(self):
        self.buildings = {}
    def add_data_from_dataframe(self, df_combined: pd.DataFrame):
        if df_combined.empty:
            return
        df_iter = df_combined.reset_index()
        for b in df_iter["Building"].unique():
            self.buildings[b] = Building(b)
        for _, row in df_iter.iterrows():
            b = row["Building"]
            self.buildings[b].add_reading(row["Timestamp"], row["kwh"])
    def calculate_campus_total(self) -> float:
        return sum(b.calculate_total_consumption() for b in self.buildings.values())

def generate_dashboard_plots(df_daily: pd.DataFrame, df_weekly: pd.DataFrame, df_combined: pd.DataFrame):
    logging.info("Generating dashboard plot.")
    sns.set_style("whitegrid")
    if not df_combined.empty:
        hourly = df_combined["kwh"].resample("H").mean().reset_index(name="kwh_hourly")
        hourly["Hour"] = hourly["Timestamp"].dt.hour
        hourly_peak = hourly.groupby(["Hour"])["kwh_hourly"].mean().reset_index()
    else:
        hourly = pd.DataFrame()
        hourly_peak = pd.DataFrame()
    if not df_weekly.empty:
        avg_weekly = df_weekly.groupby("Building")["Weekly_kwh_Total"].mean().reset_index()
    else:
        avg_weekly = pd.DataFrame(columns=["Building", "Weekly_kwh_Total"])
    fig, axes = plt.subplots(3, 1, figsize=(12, 16))
    if not df_daily.empty:
        df_daily_plot = df_daily.copy()
        df_daily_plot["Date"] = pd.to_datetime(df_daily_plot["Timestamp"]).dt.date
        sns.lineplot(data=df_daily_plot, x="Date", y="Daily_kwh_Total", hue="Building", ax=axes[0], marker="o")
        axes[0].set_title("Daily Total Energy Consumption by Building")
        axes[0].set_xlabel("Date")
        axes[0].set_ylabel("Daily kWh")
    else:
        axes[0].text(0.5, 0.5, "No daily data available", ha="center", va="center")
    if not avg_weekly.empty:
        sns.barplot(data=avg_weekly, x="Building", y="Weekly_kwh_Total", ax=axes[1])
        axes[1].set_title("Average Weekly Consumption by Building")
        axes[1].set_xlabel("Building")
        axes[1].set_ylabel("Avg Weekly kWh")
    else:
        axes[1].text(0.5, 0.5, "No weekly data available", ha="center", va="center")
    if not hourly_peak.empty:
        sns.scatterplot(data=hourly_peak, x="Hour", y="kwh_hourly", ax=axes[2], s=120)
        axes[2].set_title("Average Hourly Consumption (Campus-wide)")
        axes[2].set_xlabel("Hour of Day")
        axes[2].set_ylabel("Avg kWh")
        axes[2].set_xticks(range(0, 24, 2))
    else:
        axes[2].text(0.5, 0.5, "No hourly data available", ha="center", va="center")
    plt.tight_layout()
    out_file = OUTPUT_DIR / "dashboard.png"
    fig.savefig(out_file, dpi=150)
    plt.close(fig)
    logging.info("Dashboard saved to %s", out_file)
    return out_file

def persist_data(df_combined: pd.DataFrame, df_summary: pd.DataFrame):
    logging.info("Persisting data to disk.")
    df_combined.reset_index().to_csv(OUTPUT_DIR / "cleaned_energy_data.csv", index=False)
    df_summary.to_csv(OUTPUT_DIR / "building_summary.csv", index=False)
    logging.info("Saved cleaned_energy_data.csv and building_summary.csv")

def generate_executive_summary(manager: BuildingManager, df_daily: pd.DataFrame, df_summary: pd.DataFrame):
    total_campus_consumption = manager.calculate_campus_total()
    highest_consumer = None
    highest_kwh = 0.0
    if not df_summary.empty:
        row = df_summary.loc[df_summary["Total_kwh"].idxmax()]
        highest_consumer = row["Building"]
        highest_kwh = row["Total_kwh"]
    peak_hour_overall = None
    if not df_daily.empty:
        try:
            cleaned = pd.read_csv(OUTPUT_DIR / "cleaned_energy_data.csv", parse_dates=["Timestamp"])
            cleaned = cleaned.set_index("Timestamp")
            hourly = cleaned["kwh"].resample("H").mean()
            peak_hour_overall = int(hourly.groupby(hourly.index.hour).mean().idxmax())
        except Exception:
            peak_hour_overall = None
    daily_mean = df_daily["Daily_kwh_Total"].mean() if not df_daily.empty else 0.0
    daily_std = df_daily["Daily_kwh_Total"].std() if not df_daily.empty else 0.0
    trend_note = ("Significant variability in daily consumption, suggesting swings or scheduling issues."
                  if daily_mean and daily_std / daily_mean > 0.2 else
                  "Relatively stable daily consumption.")
    summary_text = (
        f"TOTAL CAMPUS CONSUMPTION: {total_campus_consumption:,.2f} kWh\n"
        f"HIGHEST CONSUMING BUILDING: {highest_consumer or 'N/A'} ({highest_kwh:,.2f} kWh)\n"
        f"PEAK HOUR (campus-wide average): {('Hour ' + str(peak_hour_overall) + ':00') if peak_hour_overall is not None else 'N/A'}\n"
        f"TRENDS: {trend_note}\n"
    )
    with open(OUTPUT_DIR / "summary.txt", "w") as fh:
        fh.write(summary_text)
    logging.info("Executive summary saved to %s", OUTPUT_DIR / "summary.txt")
    print(summary_text)

def main():
    logging.info("Pipeline started")
    df_combined = ingest_and_validate_data()
    if df_combined.empty:
        logging.error("No valid data to process. Exiting.")
        return
    df_daily = calculate_daily_totals(df_combined)
    df_weekly = calculate_weekly_aggregates(df_combined)
    df_summary, summary_dict = building_wise_summary(df_combined)
    manager = BuildingManager()
    manager.add_data_from_dataframe(df_combined)
    generate_dashboard_plots(df_daily, df_weekly, df_combined)
    persist_data(df_combined, df_summary)
    generate_executive_summary(manager, df_daily, df_summary)
    logging.info("Pipeline finished successfully")

if __name__ == "__main__":
    main()
