
# ⚡ Campus Energy Dashboard - Capstone Project

**Student Name:** Kartik           
**Roll Number:** 2501730166  
**Course:** Python Programming - Assignment 5 (Capstone)

---

## 📖 Overview

The **Campus Energy Dashboard** is a comprehensive data analytics application that processes energy consumption data from multiple campus buildings, performs statistical analysis, identifies trends, and generates executive dashboards with visualizations. This capstone project integrates object-oriented programming, data science libraries, and professional reporting.

---

## ✨ Key Features

- 📊 **Multi-Building Analysis:** Process energy data from multiple buildings simultaneously
- 🔍 **Data Validation:** Robust CSV parsing with error handling
- 📈 **Statistical Summaries:** Mean, min, max, and total consumption per building
- 📅 **Time-Series Trends:** Daily and weekly consumption patterns
- ⏰ **Peak Hour Detection:** Identify highest consumption times per building
- 📉 **Dashboard Generation:** 4-panel comprehensive visualization
- 💾 **Export Results:** CSV reports and PNG dashboards
- 📝 **Executive Summary:** Automated insights and key findings
- 🗂️ **Logging System:** Detailed operation logs

---

## 🚀 How to Run

### Prerequisites
```bash
pip install pandas numpy matplotlib
```

### Execution
```bash
cd ASSIGNMENT-5-CAPSTONE-PROJECT
python energy_dashboard.py
```

### Output Files
- `building_summary.csv` - Statistical summary by building
- `dashboard.png` - 4-panel visualization
- Console output with executive summary

---

## 📂 Project Structure

```
ASSIGNMENT-5-CAPSTONE-PROJECT/
├── energy_dashboard.py         # Main application
├── building_summary.csv        # Generated statistics
├── dashboard.png               # Generated visualization
├── data/                       # Energy data directory
│   ├── library_energy.csv
│   ├── engineering_energy.csv
│   └── hostel_energy.csv
└── README.md                   # This file
```

---

## 📊 Input Data Format

### CSV Requirements
Each CSV file in the `data/` directory should contain:
- `Timestamp`: Date and time of measurement
- `Building`: Building name (e.g., "Library", "Engineering")
- `kWh`: Energy consumption in kilowatt-hours

### Sample CSV Structure
```csv
Timestamp,Building,kWh
2024-11-01 00:00:00,Library,45.2
2024-11-01 01:00:00,Library,43.8
2024-11-01 02:00:00,Library,42.1
```

---

## 📈 Dashboard Panels

The generated `dashboard.png` contains four comprehensive panels:

### Panel 1: Daily Campus Energy Consumption
- **Type:** Line chart
- **Shows:** Total campus energy consumption per day
- **Purpose:** Identify daily trends and patterns

### Panel 2: Average Weekly Usage by Building
- **Type:** Bar chart
- **Shows:** Average weekly consumption for each building
- **Purpose:** Compare building efficiency

### Panel 3: Peak Hour vs Peak kWh
- **Type:** Scatter plot with annotations
- **Shows:** When each building reaches peak consumption
- **Purpose:** Optimize load distribution

### Panel 4: Executive Summary
- **Type:** Text summary
- **Shows:**
  - Total campus consumption
  - Highest-consuming building
  - Peak load information
  - Main trends

---

## 🧠 Architecture

### Object-Oriented Design

#### `BuildingManager` Class
Central class managing all energy data operations.

**Attributes:**
- `df`: Combined DataFrame with all building data
- `summary_stats`: Statistical summary per building
- `daily_totals`: Daily campus-wide totals
- `weekly_avg_by_building`: Weekly averages per building
- `peak_hours_by_building`: Peak consumption times

**Methods:**
```python
calculate_summary_statistics() -> pd.DataFrame
calculate_time_trends() -> tuple[pd.DataFrame, pd.DataFrame]
generate_dashboard_plots(output_path) -> Path
export_results(output_path) -> Path
```

---

## 📊 Analysis Pipeline

### 1. Data Ingestion
```python
def ingest_data(data_dir: Path) -> pd.DataFrame
```
- Scans `data/` directory for CSV files
- Validates column structure
- Handles malformed rows with `on_bad_lines='skip'`
- Converts timestamps to datetime
- Combines all files into single DataFrame

### 2. Statistical Analysis
```python
calculate_summary_statistics()
```
**Generates:**
- `mean_kWh`: Average consumption
- `min_kWh`: Minimum consumption
- `max_kWh`: Maximum consumption
- `total_kWh`: Total consumption

### 3. Trend Analysis
```python
calculate_time_trends()
```
**Produces:**
- Daily campus totals using `resample('D')`
- Weekly averages per building
- Peak hour identification

### 4. Visualization
```python
generate_dashboard_plots()
```
**Creates:**
- Multi-panel matplotlib figure
- Professional styling
- High-resolution PNG (150 DPI)

### 5. Export & Reporting
```python
export_results()
```
**Outputs:**
- CSV with building statistics
- Console executive summary

---

## 💡 Python Concepts Demonstrated

### Advanced OOP
- **Class Design:** Single responsibility principle
- **Encapsulation:** Private data with public methods
- **Type Hints:** Full typing with `Optional`, `tuple`
- **Property Management:** Controlled attribute access

### Data Science Stack
- **Pandas:**
  - Multi-file ingestion
  - DateTime operations
  - Groupby aggregations
  - Resampling (daily, weekly)
  - Pivot operations (`unstack`)
  
- **NumPy:**
  - Numerical computing
  - Array operations
  - Random data generation

- **Matplotlib:**
  - Subplot layouts (`2x2` grid)
  - Multiple plot types (line, bar, scatter)
  - Annotations and labels
  - Figure export

### Professional Practices
- **Logging:** Multi-level logging system
- **Error Handling:** Try-except with logging
- **Path Management:** `pathlib.Path` for cross-platform compatibility
- **Documentation:** Comprehensive docstrings
- **Code Organization:** Modular function design

---

## 📊 Output Examples

### Console Executive Summary
```text
Executive Summary
- Total campus consumption: 125,450.0 kWh
- Highest-consuming building: Engineering (52,300.0 kWh)
- Peak load time: Peak hour varies by building; see dashboard scatter.
- Main trend: Daily totals fluctuate; weekly averages highlight building usage.
```

### building_summary.csv
```csv
Building,mean_kWh,min_kWh,max_kWh,total_kWh
Engineering,55.2,42.1,68.9,52300.0
Hostel,48.5,38.2,62.1,45800.0
Library,43.1,35.5,55.3,27350.0
```

---

## 🔧 Technical Details

### Data Validation
- Checks for required columns (`Timestamp`, `Building`, `kWh`)
- Skips malformed CSV rows
- Converts data types with error handling
- Removes rows with missing critical data

### Time-Series Processing
- **Timestamp Indexing:** Sets datetime as DataFrame index
- **Resampling Frequencies:**
  - `'D'`: Daily aggregation
  - `'W'`: Weekly aggregation
- **Aggregation Functions:** `sum()`, `mean()`, `min()`, `max()`

### Peak Detection
```python
# Identifies hour and value of maximum consumption per building
df_with_hour = df.copy()
df_with_hour['Hour'] = df.index.hour
peak_hours = df.groupby('Building').apply(
    lambda g: g.loc[g['kWh'].idxmax()][['Hour', 'kWh']]
)
```

---

## 🎯 Capstone Learning Objectives

1. **Integration:** Combine multiple Python concepts in one project
2. **Real-World Application:** Solve practical energy management problems
3. **Data Pipeline:** Build end-to-end data processing workflow
4. **Visualization:** Create professional dashboards
5. **Code Quality:** Write maintainable, documented code
6. **Error Handling:** Build robust applications
7. **Reporting:** Generate actionable insights

---

## 📝 Features Highlights

### Automatic Data Simulation
If no data files exist, the program generates sample data:
```python
def _simulate_data(output_dir: Path) -> Path
```
- Creates 30 days of hourly data
- Simulates 3 buildings (Library, Engineering, Hostel)
- Includes realistic daily patterns

### Robust Error Handling
- Missing files logged and skipped
- Malformed CSV rows ignored
- Missing columns reported
- Empty datasets handled gracefully

### Professional Logging
```text
2024-12-03 10:30:15 - INFO - Ingested library_energy.csv with 720 rows.
2024-12-03 10:30:16 - INFO - Calculated summary statistics for 3 buildings.
2024-12-03 10:30:17 - INFO - Saved dashboard plot to dashboard.png
```

---

## 🔧 Requirements

### Python Version
- **Python 3.8+** (for typing features)

### Dependencies
```txt
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
```

### Installation
```bash
pip install -r requirements.txt
```

---

## 💡 Usage Scenarios

### Scenario 1: Analyze Real Data
```bash
# Place CSV files in data/ directory
python energy_dashboard.py
```

### Scenario 2: Generate Demo with Simulated Data
```bash
# Run without data/ directory to auto-generate samples
python energy_dashboard.py
```

### Scenario 3: Programmatic Usage
```python
from energy_dashboard import ingest_data, BuildingManager
from pathlib import Path

# Load custom data
df = ingest_data(Path('my_data'))

# Analyze
manager = BuildingManager(df)
manager.calculate_summary_statistics()
manager.calculate_time_trends()
manager.generate_dashboard_plots(Path('.'))
manager.export_results(Path('.'))
```

---

## 📖 Advanced Features

### Multi-Building Comparison
- Side-by-side analysis of multiple facilities
- Normalized metrics for fair comparison
- Building-specific insights

### Temporal Analysis
- Daily trends for short-term patterns
- Weekly averages for medium-term planning
- Peak hour detection for load management

### Visual Analytics
- Color-coded plots for clarity
- Annotations for key data points
- Professional layout with `tight_layout()`

---

## 🎯 Project Impact

### Use Cases
- **Campus Administration:** Monitor energy consumption
- **Facility Management:** Identify inefficient buildings
- **Sustainability:** Track carbon footprint reduction
- **Budget Planning:** Forecast energy costs
- **Load Management:** Optimize peak hour distribution

### Insights Provided
1. Which building consumes the most energy?
2. What are the daily consumption trends?
3. When do peak loads occur?
4. How does weekly usage vary?
5. What is the total campus footprint?

---

## 🐛 Troubleshooting

### No Data Files
**Issue:** `No CSV files found in data directory`  
**Solution:** Add CSV files to `data/` or let program generate samples

### Missing Columns
**Issue:** `Missing 'Timestamp' column in file.csv`  
**Solution:** Ensure CSV has required columns: Timestamp, Building, kWh

### Import Errors
**Issue:** `ModuleNotFoundError: No module named 'pandas'`  
**Solution:** Run `pip install pandas numpy matplotlib`

---

## 👨‍💻 Author

**Kartik**                
Roll Number: 2501730166  
B.Tech CSE (AI & ML)  
K.R. Mangalam University

---

## 🏆 Capstone Achievement

This project demonstrates mastery of:
- ✅ Object-Oriented Programming
- ✅ Data Analysis with Pandas
- ✅ Statistical Computing
- ✅ Data Visualization
- ✅ File I/O Operations
- ✅ Error Handling
- ✅ Logging Systems
- ✅ Professional Code Documentation

---

## 📄 License

This project is created for educational purposes as part of Python Programming coursework.

---

## 🔮 Future Enhancements

- Real-time data streaming
- Database integration
- Web dashboard interface
- Predictive analytics with ML
- Anomaly detection
- Cost analysis integration
