# SWYNEX — Data Cleaning & Preparation

## Project overview
This project demonstrates data cleaning with Python and Pandas for SWYNEX Task 1. It includes a raw practice file, a cleaned dataset, reproducible code, and a cleaning report.

## Dataset and source
The underlying public dataset is the **Iris dataset** from the UCI Machine Learning Repository:
https://archive.ics.uci.edu/dataset/53/iris

The Iris dataset is a well-known public dataset of flower measurements and species. To make this task suitable for practicing data cleaning, I created `raw_iris_data.csv` as a **messy practice copy** based on the public source and deliberately introduced a small number of data-quality defects (such as inconsistent labels, missing markers, a duplicate row, and implausible measurements). These injected issues are not claimed to be present in the original UCI dataset.

## Files
- `raw_iris_data.csv` — practice copy with documented data-quality issues.
- `cleaned_iris_data.csv` — cleaned dataset ready for analysis.
- `clean_data.py` — reproducible Python cleaning script.
- `cleaning_report.json` — machine-readable summary of cleaning steps and results.

## Problems identified and actions taken
1. **Duplicate records:** removed exact duplicate rows.
2. **Missing values:** recognized blank cells and markers such as `N/A`, `missing`, and `not recorded`.
3. **Incorrect data types:** converted measurement columns from text to numeric values.
4. **Inconsistent values:** trimmed spaces and standardized species labels to lowercase.
5. **Typographical inconsistency:** mapped `versicolour` to `versicolor`.
6. **Invalid measurements:** treated values outside a generous 0.1–10 cm range as missing for review.
7. **Missing numeric data:** filled missing measurements using the median within the same species.

## How to run
Requires Python 3 and Pandas.

```bash
pip install pandas
python clean_data.py
```

The script reads `raw_iris_data.csv` and writes `cleaned_iris_data.csv`.

## Validation
The script prints the row counts, number of exact duplicate rows removed, and remaining missing values. Review the cleaned output before using it for further analysis.

## Assumptions and limitations
- This is a learning project, not a scientific re-analysis of the Iris dataset.
- Data-quality defects were deliberately introduced to demonstrate cleaning methods.
- The 0.1–10 cm plausibility check is a simple teaching rule, not a universal botanical rule.
- Median imputation preserves rows but may affect later statistical analysis; in a real project, justify the choice or retain missing values where appropriate.
