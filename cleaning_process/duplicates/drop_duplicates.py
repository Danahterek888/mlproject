
import os
import pandas as pd

# === Paths ===
train_csv = "../../initial Dataset/ethnicity-classifier-train.csv"
val_csv   = "../../initial Dataset/ethnicity-classifier-val.csv"
train_output = "../../final Dataset/cleaned_ethnicity-classifier-train.csv"
val_output   = "../../final Dataset/cleaned_ethnicity-classifier-val.csv"

# === Load TRAIN CSV ===
df_train = pd.read_csv(train_csv)
print(f"📄 TRAIN original rows: {df_train.shape[0]}")

# === Drop duplicates in TRAIN ===
df_train_cleaned = df_train.drop_duplicates().reset_index(drop=True)
print(f"✅ TRAIN duplicates removed. Remaining rows: {df_train_cleaned.shape[0]}")

# === Save cleaned TRAIN version ===
os.makedirs("../../final Dataset", exist_ok=True)
df_train_cleaned.to_csv(train_output, index=False)
print(f"💾 Saved cleaned TRAIN dataset to '{train_output}'")

# === Load VAL CSV ===
df_val = pd.read_csv(val_csv)
print(f"\n📄 VAL original rows: {df_val.shape[0]}")

# === Drop duplicates in VAL ===
df_val_cleaned = df_val.drop_duplicates().reset_index(drop=True)
print(f"✅ VAL duplicates removed. Remaining rows: {df_val_cleaned.shape[0]}")

# === Save cleaned VAL version ===
df_val_cleaned.to_csv(val_output, index=False)
print(f"💾 Saved cleaned VAL dataset to '{val_output}'")
