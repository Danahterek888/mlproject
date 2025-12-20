import os
import pandas as pd

# === Paths ===
input_csv = "../../initial Dataset/ethnicity-classifier.csv"
output_path = "../../final Dataset/cleaned_ethnicity-classifier.csv"

# === Load dataset ===
df = pd.read_csv(input_csv)
print(f"📄 Original rows: {df.shape[0]}")

# === Drop null rows ===
df_cleaned = df.dropna().reset_index(drop=True)
print(f"✅ Nulls removed. Remaining rows: {df_cleaned.shape[0]}")

# === Save cleaned dataset ===
os.makedirs("../../final Dataset", exist_ok=True)
df_cleaned.to_csv(output_path, index=False)
print(f"💾 Cleaned dataset saved to: {output_path}")
