import os
import pandas as pd

# === Paths ===
input_csv = "../../initial Dataset/ethnicity-classifier.csv"
output_path = "../../final Dataset/cleaned_ethnicity-classifier.csv"

# === Load CSV ===
df = pd.read_csv(input_csv)
print(f"📄 Original rows: {df.shape[0]}")

# === Drop duplicates ===
df_cleaned = df.drop_duplicates().reset_index(drop=True)
print(f"✅ Duplicates removed. Remaining rows: {df_cleaned.shape[0]}")

# === Save cleaned version ===
os.makedirs("../../final Dataset", exist_ok=True)
df_cleaned.to_csv(output_path, index=False)
print(f"💾 Saved cleaned dataset to '{output_path}'")
