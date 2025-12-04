import sys
from typing import Tuple
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_and_clean_data(file_path: str) -> pd.DataFrame:
    """
    Loads a CSV file, converts the 'Date' column to datetime,
    sets it as the index, and fills missing numeric values using
    time-based linear interpolation.
    """
    # Read file
    data = pd.read_csv(file_path)

    # Validate presence of Date column
    if "Date" not in data.columns:
        raise ValueError("Input CSV must contain a 'Date' column.")

    # Convert date and set as index
    data["Date"] = pd.to_datetime(data["Date"])
    data = data.sort_values("Date").set_index("Date")

    # Interpolate numeric fields
    numeric_fields = data.select_dtypes(include=[np.number]).columns
    if numeric_fields.any():
        data[numeric_fields] = data[numeric_fields].interpolate(
            method="linear", limit_direction="both"
        )

    return data


def analyze_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregates daily weather data into monthly metrics:
      - Average, minimum, maximum temperature
      - Total rainfall
    Returns a new DataFrame indexed by month-end.
    """

    required_cols = ["Temperature_C", "Rainfall_mm"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Monthly resampling
    mean_temp = df["Temperature_C"].resample("ME").mean()
    min_temp = df["Temperature_C"].resample("ME").min()
    max_temp = df["Temperature_C"].resample("ME").max()
    sum_rain = df["Rainfall_mm"].resample("ME").sum()

    monthly = pd.DataFrame({
        "MonthlyMeanTemp": mean_temp,
        "MonthlyMinTemp": min_temp,
        "MonthlyMaxTemp": max_temp,
        "MonthlyTotalRainfall": sum_rain
    })

    return monthly


def create_visualizations(df_monthly: pd.DataFrame) -> Tuple[plt.Figure, plt.Axes]:
    """
    Builds three visualizations:
      1. Line plot of monthly mean temperatures
      2. Bar chart of monthly rainfall totals
      3. Combined chart using a dual y-axis
    Returns the combined chart (figure and main axis).
    """

    # Mean temperature line chart
    fig_a, ax_a = plt.subplots(figsize=(10, 4))
    ax_a.plot(df_monthly.index, df_monthly["MonthlyMeanTemp"],
              linewidth=2, color="tab:red")
    ax_a.set_title("Average Temperature by Month")
    ax_a.set_xlabel("Month")
    ax_a.set_ylabel("Temperature (°C)")
    fig_a.tight_layout()

    # Rainfall bar chart
    fig_b, ax_b = plt.subplots(figsize=(10, 4))
    ax_b.bar(df_monthly.index, df_monthly["MonthlyTotalRainfall"],
             width=20, color="tab:blue")
    ax_b.set_title("Total Monthly Rainfall")
    ax_b.set_xlabel("Month")
    ax_b.set_ylabel("Rainfall (mm)")
    fig_b.tight_layout()

    # Combined plot
    fig_c, ax_c = plt.subplots(figsize=(11, 5))
    ax_c.plot(df_monthly.index, df_monthly["MonthlyMeanTemp"],
              linewidth=2, color="tab:red", label="Mean Temp (°C)")
    ax_c.set_xlabel("Month")
    ax_c.set_ylabel("Temperature (°C)", color="tab:red")
    ax_c.tick_params(axis="y", labelcolor="tab:red")

    ax_c2 = ax_c.twinx()
    ax_c2.bar(df_monthly.index, df_monthly["MonthlyTotalRainfall"],
              width=20, color="tab:blue", alpha=0.6, label="Rainfall (mm)")
    ax_c2.set_ylabel("Rainfall (mm)", color="tab:blue")
    ax_c2.tick_params(axis="y", labelcolor="tab:blue")

    # Merge legends
    line_handles, line_labels = ax_c.get_legend_handles_labels()
    bar_handles, bar_labels = ax_c2.get_legend_handles_labels()
    ax_c.legend(line_handles + bar_handles,
                line_labels + bar_labels,
                loc="upper left")

    fig_c.suptitle("Monthly Weather Overview")
    fig_c.tight_layout()

    return fig_c, ax_c


def main(argv=None):
    argv = argv or sys.argv[1:]

    if len(argv) < 1:
        print("Usage: python script.py <weather_data.csv>")
        print("Expected columns: Date, Temperature_C, Rainfall_mm")
        return 1

    csv_path = argv[0]
    df = load_and_clean_data(csv_path)
    summary = analyze_data(df)
    fig, _ = create_visualizations(summary)

    output_file = "weather_summary_plot.png"
    fig.savefig(output_file, dpi=150)
    print(f"Saved chart to {output_file}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
