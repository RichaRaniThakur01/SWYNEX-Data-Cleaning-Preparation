"""
SWYNEX Task 1 — Data Cleaning & Preparation
Source dataset: UCI Machine Learning Repository, Iris dataset.
This script uses raw_iris_data.csv, a messy practice copy derived from the public dataset.
Run: pip install pandas && python clean_data.py
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "raw_iris_data.csv"
OUTPUT = ROOT / "cleaned_iris_data.csv"

df = pd.read_csv(INPUT, dtype="string")
rows_before = len(df)
duplicates_removed = int(df.duplicated().sum())
df = df.drop_duplicates().copy()

numeric_cols = [
    "sepal_length_cm", "sepal_width_cm",
    "petal_length_cm", "petal_width_cm"
]
for col in numeric_cols:
    df[col] = (
        df[col].str.strip()
        .str.replace(",", ".", regex=False)
        .replace({
            "": pd.NA, "N/A": pd.NA, "missing": pd.NA,
            "not recorded": pd.NA, "na": pd.NA, "NA": pd.NA
        })
    )
    df[col] = pd.to_numeric(df[col], errors="coerce")
    # Flag implausible measurements as missing for review.
    df.loc[~df[col].between(0.1, 10), col] = pd.NA

# Standardize category labels and fix a known spelling variant.
df["species"] = df["species"].str.strip().str.lower()
df["species"] = df["species"].replace({"versicolour": "versicolor"})
df = df[df["species"].isin(["setosa", "versicolor", "virginica"])].copy()

# Fill missing measurements with the median for the same species.
for col in numeric_cols:
    df[col] = df.groupby("species")[col].transform(
        lambda values: values.fillna(values.median())
    )

df["record_id"] = pd.to_numeric(df["record_id"], errors="coerce").astype("Int64")
df = df[["record_id"] + numeric_cols + ["species"]]
df.to_csv(OUTPUT, index=False, float_format="%.1f")

print(f"Rows before cleaning: {rows_before}")
print(f"Exact duplicate rows removed: {duplicates_removed}")
print(f"Rows after cleaning: {len(df)}")
print("Missing values after cleaning:")
print(df.isna().sum())
print(f"Cleaned file saved to: {OUTPUT}")
