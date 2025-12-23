
import os
import pandas as pd

# === Paths ===
train_csv = "../../initial Dataset/ethnicity-classifier-train.csv"
val_csv   = "../../initial Dataset/ethnicity-classifier-val.csv"
output_dir = "."
os.makedirs(output_dir, exist_ok=True)

# === Load CSVs ===
df_train = pd.read_csv(train_csv)
df_val   = pd.read_csv(val_csv)

# === Find duplicates in TRAIN ===
duplicates_train = df_train[df_train.duplicated()]
print(f"\n📎 Found {duplicates_train.shape[0]} duplicate rows in TRAIN")

# === Save train duplicates to CSV
if not duplicates_train.empty:
    output_path_train = os.path.join(output_dir, "duplicates_backup_train.csv")
    duplicates_train.to_csv(output_path_train, index=False)
    print(f"💾 Saved to '{output_path_train}'")
else:
    print("✅ No duplicates found in TRAIN.")

# === Find duplicates in VAL ===
duplicates_val = df_val[df_val.duplicated()]
print(f"\n📎 Found {duplicates_val.shape[0]} duplicate rows in VAL")

# === Save val duplicates to CSV
if not duplicates_val.empty:
    output_path_val = os.path.join(output_dir, "duplicates_backup_val.csv")
    duplicates_val.to_csv(output_path_val, index=False)
    print(f"💾 Saved to '{output_path_val}'")
else:
    print("✅ No duplicates found in VAL.")
