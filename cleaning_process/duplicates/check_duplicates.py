import os
import pandas as pd

# === Paths ===
input_csv = "../../initial Dataset/ethnicity-classifier.csv"
output_dir = "."
os.makedirs(output_dir, exist_ok=True)

# === Load CSV ===
df = pd.read_csv(input_csv)

# === Find duplicates ===
duplicates = df[df.duplicated()]
print(f"\n📎 Found {duplicates.shape[0]} duplicate rows")

# === Save duplicates to CSV
if not duplicates.empty:
    output_path = os.path.join(output_dir, "duplicates_backup.csv")
    duplicates.to_csv(output_path, index=False)
    print(f"💾 Saved to '{output_path}'")
else:
    print("✅ No duplicates found.")
