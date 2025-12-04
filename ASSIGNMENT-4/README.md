# 🌤️ Weather Data Analysis Tool

**Student Name:** Kartik       
**Roll Number:** 2501730166  
**Course:** Python Programming - Assignment 4

---

## 📖 Overview

The **Weather Data Analysis Tool** is a Python application that processes weather data from CSV files, performs time-series analysis, and generates visualizations. It demonstrates data manipulation with pandas, statistical analysis with numpy, and visualization with matplotlib.

---

## ✨ Features

- 📊 **Data Processing:** Automatic CSV loading and cleaning
- 🔍 **Missing Data Handling:** Linear interpolation for gaps
- 📅 **Time-Series Analysis:** Monthly aggregation and resampling
- 📈 **Statistical Metrics:** Mean, min, max temperature; total rainfall
- 📉 **Visualizations:** 
  - Line charts for temperature trends
  - Bar charts for rainfall distribution
  - Combined dual-axis plots
- 💾 **Export Plots:** High-resolution PNG output

---

## 🚀 How to Run

1. **Navigate to the project directory:**
   ```bash
   cd ASSIGNMENT-4
   ```

2. **Install required dependencies:**
   ```bash
   pip install pandas numpy matplotlib
   ```

3. **Run the program:**
   ```bash
   python weather_analysis.py sample_weather.csv
   ```

4. **View the output:**
   - Console: Monthly statistics
   - File: `output_plot.png` (combined visualization)

---

## 📋 Command Line Usage

```bash
python weather_analysis.py <path_to_csv>
```

**Example:**
```bash
python weather_analysis.py sample_weather.csv
```

---

## 📊 Input Data Format

### CSV Requirements
The CSV file must contain these columns:
- `Date`: Date in parseable format (YYYY-MM-DD, DD/MM/YYYY, etc.)
- `Temperature_C`: Temperature in Celsius
- `Rainfall_mm`: Rainfall in millimeters

### Sample CSV
```csv
Date,Temperature_C,Rainfall_mm
2024-01-01,15.5,0.0
2024-01-02,16.2,5.3
2024-01-03,14.8,12.1
2024-01-04,,8.5
2024-01-05,15.9,0.0
```

**Note:** Missing values (empty cells) are automatically filled using linear interpolation.

---

## 📈 Output

### Console Output
```text
Saved combined plot to output_plot.png
```

### Generated File
- `output_plot.png`: High-resolution (150 DPI) combined visualization

---

## 📊 Visualizations

The tool generates three types of plots:

### 1. Monthly Mean Temperature (Line Chart)
- **X-axis:** Month
- **Y-axis:** Temperature (°C)
- **Color:** Red
- Shows temperature trends over time

### 2. Monthly Total Rainfall (Bar Chart)
- **X-axis:** Month
- **Y-axis:** Rainfall (mm)
- **Color:** Blue
- Displays monthly precipitation totals

### 3. Combined Plot (Dual-Axis)
- **Left Y-axis:** Temperature (°C) - Red line
- **Right Y-axis:** Rainfall (mm) - Blue bars
- **X-axis:** Month
- Allows comparison of temperature and rainfall patterns

---

## 🧠 Python Concepts Demonstrated

### Data Analysis Libraries
- **Pandas:** 
  - `read_csv()`: Load data
  - `to_datetime()`: Parse dates
  - `set_index()`: Time-series indexing
  - `resample()`: Monthly aggregation
  - `interpolate()`: Fill missing values
  - `groupby()`: Data aggregation

- **NumPy:**
  - `select_dtypes()`: Column filtering
  - Numerical operations

- **Matplotlib:**
  - `subplots()`: Create figure layouts
  - `plot()`: Line charts
  - `bar()`: Bar charts
  - `twinx()`: Dual-axis plotting
  - `savefig()`: Export images

### Programming Concepts
- **Type Hints:** Function signatures with types
- **Error Handling:** ValueError exceptions
- **Command-Line Arguments:** `sys.argv` processing
- **Data Cleaning:** Missing value imputation
- **Datetime Operations:** Date parsing and manipulation
- **Statistical Methods:** `mean()`, `min()`, `max()`, `sum()`

---

## 📂 File Structure

```
ASSIGNMENT-4/
├── weather_analysis.py     # Main application
├── sample_weather.csv      # Sample data file
├── output_plot.png         # Generated visualization
└── README.md               # This file
```

---

## 🔧 Technical Details

### Data Processing Pipeline

1. **Load Data**
   - Read CSV with pandas
   - Parse Date column to datetime
   - Sort by date

2. **Clean Data**
   - Set Date as index
   - Identify numeric columns
   - Apply linear interpolation for missing values

3. **Analyze Data**
   - Resample to monthly frequency ('ME')
   - Calculate temperature statistics (mean, min, max)
   - Sum rainfall totals

4. **Visualize Results**
   - Create matplotlib figures
   - Apply formatting and labels
   - Save high-resolution plots

---

## 📊 Monthly Analysis Metrics

| Metric | Description | Calculation |
|--------|-------------|-------------|
| **MonthlyMeanTemp** | Average temperature | `resample('ME').mean()` |
| **MonthlyMinTemp** | Minimum temperature | `resample('ME').min()` |
| **MonthlyMaxTemp** | Maximum temperature | `resample('ME').max()` |
| **MonthlyTotalRainfall** | Total precipitation | `resample('ME').sum()` |

---

## 💡 Usage Examples

### Example 1: Basic Analysis
```bash
python weather_analysis.py sample_weather.csv
```

### Example 2: Custom Data File
```bash
python weather_analysis.py my_weather_data.csv
```

### Example 3: Programmatic Usage
```python
from weather_analysis import load_and_clean_data, analyze_data, create_visualizations

# Load and process data
df = load_and_clean_data('sample_weather.csv')
df_monthly = analyze_data(df)
fig, ax = create_visualizations(df_monthly)

# Save or display
fig.savefig('my_plot.png', dpi=150)
```

---

## 🔧 Requirements

### Python Version
- **Python 3.7+** (for type hints and f-strings)

### Dependencies
```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
```

### Installation
```bash
pip install pandas numpy matplotlib
```

---

## ⚠️ Error Handling

The program handles several error conditions:

### Missing Date Column
```python
ValueError: CSV must contain a 'Date' column
```

### Missing Temperature Column
```python
ValueError: DataFrame must contain 'Temperature_C' column
```

### Missing Rainfall Column
```python
ValueError: DataFrame must contain 'Rainfall_mm' column
```

### Invalid File Path
```python
FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent.csv'
```

---

## 📝 Features Highlights

### Automatic Data Cleaning
- Detects and fills missing values
- Sorts data chronologically
- Converts dates automatically

### Flexible Date Parsing
Accepts various date formats:
- `2024-01-01`
- `01/01/2024`
- `2024/01/01`
- `Jan 1, 2024`

### High-Quality Visualizations
- 150 DPI resolution
- Clear axis labels
- Color-coded data
- Professional styling

---

## 🎯 Learning Objectives

1. **Data Analysis:** Pandas for time-series manipulation
2. **Statistical Computing:** NumPy for numerical operations
3. **Visualization:** Matplotlib for creating plots
4. **Data Cleaning:** Handling missing values
5. **Type Safety:** Using type hints
6. **CLI Development:** Command-line argument processing
7. **Error Handling:** Robust exception management

---

## 📖 Additional Notes

### Resample Frequency
- Uses `'ME'` (month-end) for monthly resampling
- Replaces deprecated `'M'` to avoid FutureWarning

### Interpolation Method
- Linear interpolation fills gaps smoothly
- Bidirectional (`limit_direction='both'`)
- Suitable for weather data continuity

### Plot Customization
- Modify colors, widths, and styles in source code
- Adjust DPI for different resolutions
- Change figure sizes for presentations

---

## 👨‍💻 Author

**Kartik**        
Roll Number: 2501730166  
B.Tech CSE (AI & ML)  
K.R. Mangalam University

---

## 📄 License

This project is created for educational purposes as part of Python Programming coursework.
