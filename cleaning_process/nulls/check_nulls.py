import os
import pandas as pd

# === Paths ===
input_csv = "../../initial Dataset/ethnicity-classifier.csv"
output_dir = "."
os.makedirs(output_dir, exist_ok=True)

# === Load CSV ===
df = pd.read_csv(input_csv)

# === Nulls Summary by Column ===
null_counts = df.isnull().sum()
null_summary = null_counts[null_counts > 0]

if not null_summary.empty:
    print("\n📊 Nulls found in the following columns:")
    print(null_summary)

    # === Save rows with any nulls ===
    null_rows = df[df.isnull().any(axis=1)]
    null_rows.to_csv(os.path.join(output_dir, "null_rows_backup.csv"), index=False)
    print("💾 Rows with nulls saved to 'null_rows_backup.csv'")
else:
    print("✅ No nulls found in any column.")
