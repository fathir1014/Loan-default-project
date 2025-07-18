import os
import joblib
from sklearn.linear_model import LogisticRegression

def train_model(X, y, scaler, emp_encoder, mar_encoder, save_dir="model"):
    # Inisialisasi model Logistic Regression
    model = LogisticRegression(class_weight='balanced', max_iter=1000)
    model.fit(X, y)

    # Buat folder penyimpanan jika belum ada
    os.makedirs(save_dir, exist_ok=True)

    # Simpan model
    joblib.dump(model, os.path.join(save_dir, "logistic_model.pkl"))
    print("[INFO] Model Logistic Regression disimpan.")

    # Simpan scaler
    joblib.dump(scaler, os.path.join(save_dir, "scaler.pkl"))
    print("[INFO] Scaler disimpan.")

    # Simpan encoder
    joblib.dump(emp_encoder, os.path.join(save_dir, "emp_encoder.pkl"))
    joblib.dump(mar_encoder, os.path.join(save_dir, "mar_encoder.pkl"))
    print("[INFO] Encoder disimpan.")

    return model
