import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "outputs" / "CLRI_Final_Results.csv"

df = pd.read_csv(path)

print("Rows:", len(df))
print("Columns:", list(df.columns))

clri_cols = [c for c in df.columns if c.startswith("CLRI_")]
print("\nCLRI summary:")
print(df[clri_cols].describe().round(4))

for col in ["Equal_Category", "Entropy_Category", "CRITIC_Category", "PCA_Category"]:
    if col in df:
        print(f"\n{col}:")
        print(df[col].value_counts())
