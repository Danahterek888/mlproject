

import os
import pandas as pd

# === Paths ===
train_csv = "../../initial Dataset/ethnicity-classifier-train.csv"
val_csv   = "../../initial Dataset/ethnicity-classifier-val.csv"
output_dir = "."
os.makedirs(output_dir, exist_ok=True)

# === Load TRAIN CSV ===
df_train = pd.read_csv(train_csv)

# === Nulls Summary by Column (TRAIN) ===
null_counts_train = df_train.isnull().sum()
null_summary_train = null_counts_train[null_counts_train > 0]

if not null_summary_train.empty:
    print("\n📊 Nulls found in the following columns (TRAIN):")
    print(null_summary_train)

    # === Save rows with any nulls (TRAIN) ===
    null_rows_train = df_train[df_train.isnull().any(axis=1)]
    null_rows_train.to_csv(os.path.join(output_dir, "null_rows_backup_train.csv"), index=False)
    print("💾 Rows with nulls saved to 'null_rows_backup_train.csv'")
else:
    print("✅ No nulls found in any column (TRAIN).")

# === Load VAL CSV ===
df_val = pd.read_csv(val_csv)

# === Nulls Summary by Column (VAL) ===
null_counts_val = df_val.isnull().sum()
null_summary_val = null_counts_val[null_counts_val > 0]

if not null_summary_val.empty:
    print("\n📊 Nulls found in the following columns (VAL):")
    print(null_summary_val)

    # === Save rows with any nulls (VAL) ===
    null_rows_val = df_val[df_val.isnull().any(axis=1)]
    null_rows_val.to_csv(os.path.join(output_dir, "null_rows_backup_val.csv"), index=False)
    print("💾 Rows with nulls saved to 'null_rows_backup_val.csv'")
else:
    print("✅ No nulls found in any column (VAL).")