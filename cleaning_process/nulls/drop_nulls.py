
import os
import pandas as pd

# === Paths ===
train_csv = "../../initial Dataset/ethnicity-classifier-train.csv"
val_csv   = "../../initial Dataset/ethnicity-classifier-val.csv"
train_output = "../../final Dataset/cleaned_ethnicity-classifier-train.csv"
val_output   = "../../final Dataset/cleaned_ethnicity-classifier-val.csv"

# === Load TRAIN dataset ===
df_train = pd.read_csv(train_csv)
print(f"📄 TRAIN original rows: {df_train.shape[0]}")

# === Drop null rows (TRAIN) ===
df_train_cleaned = df_train.dropna().reset_index(drop=True)
print(f"✅ TRAIN nulls removed. Remaining rows: {df_train_cleaned.shape[0]}")

# === Save cleaned TRAIN dataset ===
os.makedirs("../../final Dataset", exist_ok=True)
df_train_cleaned.to_csv(train_output, index=False)
print(f"💾 Cleaned TRAIN dataset saved to: {train_output}")

# === Load VAL dataset ===
df_val = pd.read_csv(val_csv)
print(f"\n📄 VAL original rows: {df_val.shape[0]}")

# === Drop null rows (VAL) ===
df_val_cleaned = df_val.dropna().reset_index(drop=True)
print(f"✅ VAL nulls removed. Remaining rows: {df_val_cleaned.shape[0]}")

# === Save cleaned VAL dataset ===
df_val_cleaned.to_csv(val_output, index=False)
print(f"💾 Cleaned VAL dataset saved to: {val_output}")
