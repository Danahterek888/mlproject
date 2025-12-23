# MLPROJECT: Ethnicity Classification from Facial Images

This project builds a machine learning pipeline that classifies a person's ethnicity based on facial image features. It includes dataset preprocessing, cleaning, and preparation for model training using classical machine learning algorithms.

---

## 📁 Project Structure

```
MLPROJECT/
├── cleaning_process/
│   ├── duplicates/
│   │   ├── check_duplicates.py
│   │   ├── drop_duplicates.py
│   │   └── duplicates_backup.csv
│   ├── nulls/
│   │   ├── check_nulls.py
│   │   ├── drop_nulls.py
│   │   └── null_rows_backup.csv
├── initial Dataset/
│   └── ethnicity-classifier.csv
├── final Dataset/
│   └── cleaned_ethnicity-classifier.csv
├── train/               ← (ignored by .gitignore)
├── main.py
└── .gitignore
```

---

## ✅ Cleaning Process

- Checked and removed **duplicate records** (stored in `duplicates_backup.csv`)
- Identified and dropped **rows with null values** (stored in `null_rows_backup.csv`)
- Final cleaned dataset is stored in:  
  `final Dataset/cleaned_ethnicity-classifier.csv`

---

## ⚙️ Technologies & Libraries

- **Python 3.10+**
- `pandas`, `numpy`
- `scikit-learn`, `matplotlib`
- `Pillow`, `scikit-image`

---

## 🔄 Next Steps

-- Perform feature extraction using **Convolutional Neural Networks (CNN)**
- Train models such as:
- SVM (Support Vector Machine)
- KNN (K-Nearest Neighbors)
- Random Forest
- Evaluate model performance and accuracy

---

## 👥 Authors

- Joelle Sarkis
- Danah el Terek
- Samir Najib

---

## 📝 License

This project is for academic purposes only.
