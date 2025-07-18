import pandas as pd
import joblib
import os

def predict_single(data_dict):
    """
    Menerima input dictionary berisi data user baru,
    mengembalikan prediksi default (0 atau 1).
    """
    # Load model dan preprocessing tools
    model = joblib.load("loan_default_project/model/model.pkl")
    scaler = joblib.load("loan_default_project/model/scaler.pkl")
    emp_encoder = joblib.load("loan_default_project/model/emp_encoder.pkl")
    mar_encoder = joblib.load("loan_default_project/model/mar_encoder.pkl")

    # Ubah ke DataFrame
    df = pd.DataFrame([data_dict])

    # Encode kolom kategorikal
# Encode
    df["employment_status"] = emp_encoder.transform(df["employment_status"])
    df["marital_status"] = mar_encoder.transform(df["marital_status"])

# Scaling numerik
    numerical_cols = ["age", "income", "loan_amount", "loan_term_months", "credit_score"]
    df[numerical_cols] = scaler.transform(df[numerical_cols])

# URUTKAN KOLON SESUAI TRAINING 
    df = df[model.feature_names_in_]

# Prediksi
    pred = model.predict(df)[0]
    proba = model.predict_proba(df)[0][1]
    
    # Output
    print(f"[PREDIKSI] Hasil prediksi: {'DEFAULT' if pred == 1 else 'TIDAK DEFAULT'} (Probabilitas: {proba:.2%})")
    return pred, proba

# Contoh penggunaan
if __name__ == "__main__":
    data_baru = {
        "age": 35,
        "income": 7500,
        "loan_amount": 3000,
        "loan_term_months": 24,
        "credit_score": 680,
        "employment_status": "Employed",
        "marital_status": "Married"
    }
    predict_single(data_baru)
