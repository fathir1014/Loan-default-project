# 🧠 Loan Default Prediction System

A machine learning project built to predict whether a customer will default on their loan or not — based on their demographic and financial data.

## 📌 Project Overview

This system takes in customer loan application data (Excel format), processes it, trains a classification model (Logistic Regression), and returns predictions on whether each customer will default.

The model includes:
- Data cleaning & encoding
- Feature scaling
- Model training & evaluation
- Exporting predictions
- Saving model & scalers for future use

---

## 📂 Project Structure

loan_default_project/
├── main.py # Entry point
├── config/ # Configuration files (if needed)
├── data/ # Input Excel data
├── loader/ # Data loading module
├── preprocessing/ # Data cleaning, encoding, scaling
├── model/ # Training & evaluation logic
├── predictor/ # Predict new inputs using saved model
├── export/ # Output results to Excel
├── utils/ # Logging, formatting helpers
└── README.md # You're reading it!


---

## 🛠️ How It Works

1. 📥 **Load Data**: From Excel (loan_data.xlsx)
2. 🧹 **Preprocess**: Drop unused columns, handle missing values, encode categoricals, scale numerics
3. 🧪 **Train Model**: Logistic Regression classifier
4. 📊 **Evaluate**: Accuracy, precision, recall, F1-score, confusion matrix
5. 🧠 **Predict**: For new customers or test data
6. 📤 **Export**: Save prediction results to Excel
7. 💾 **Save Model**: Trained model, scaler, and encoders saved for reuse

---

## 🧪 Example Features Used

- Age  
- Income  
- Loan Amount  
- Loan Term  
- Credit Score  
- Employment Status *(encoded)*  
- Marital Status *(encoded)*

---

## 🚀 Tech Stack

- Python
- Pandas
- Scikit-learn
- Joblib (for model persistence)
- Excel I/O (`pd.read_excel`, `to_excel`)

---

## 📦 Output

After running the system, you'll get:
- A trained model file (`model.pkl`)
- Encoders & scaler files
- Excel file with predictions
- Evaluation metrics summary

---

## ✍️ Author

**Fathir** – AI Developer, Python Specialist, Data-Driven Freelancer.

---

## 📞 Contact

Want this kind of system for your business?  
Reach out via Upwork, GitHub, or email.

Upwork : Fathir Rizki F
Github : Fathir1014
Email : fathirrf80@gmail.com
