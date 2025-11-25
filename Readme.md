# 📘 GradeBook Analyzer

**Student Name:** Kartik       
**Roll Number:** 2501730166
**Course:** Python Programming

## 📝 Project Description

The **GradeBook Analyzer** is a Python command-line tool designed to help teachers and students manage and analyze student marks efficiently. It allows users to enter data manually or load it from a CSV file to automatically calculate averages, assign grades, and generate a statistical report.

## ✨ Features

* **Manual Entry:** Type student names and marks directly into the program.
  * **CSV Import:** Load a list of students from a `.csv` file.
  * **Add Student:** Append a new student record to an existing CSV file.
  * **Automatic Grading:** Assigns letter grades (A, B, C, D, F) based on scores.
  * **Statistics:** meaningful analysis including:
    * Class Average
    * Highest and Lowest Scores
    * Pass/Fail Counts
    * Grade Distribution

## 🚀 How to Run

1. Ensure you have **Python** installed.
2. Download the `gradebook.py` file.
3. Open your terminal or command prompt.
4. Navigate to the folder containing the file.
5. Run the following command:

    ```bash
       python gradebook.py
    ```

## 📋 Usage Guide

When you run the program, you will see a menu with 4 options:

1. **Manual Entry:** Enter names and marks one by one. Type `done` when finished to see the report.
2. **Load from CSV:** Type the name of an existing CSV file (e.g., `marks.csv`) to load data and view the report.
3. **Add Student to CSV:** Add a single student's name and mark to a CSV file. If the file doesn't exist, it will be created.
4. **Exit:** Close the program.

## 📂 CSV File Format

If you create your own CSV file, it should look like this (the first row is the header):

```csv
Name,Marks
Alice,85
Bob,92
Charlie,68
```

* **Column 1:** Student Name
* **Column 2:** Marks (Numeric)
