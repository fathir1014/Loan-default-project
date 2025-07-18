import pandas as pd
from loader.data_loader import load_loan_data
from preprocessing.clean_data import preprocess
from model.trainer import train_model
from model.evaluator import evaluate_model
from predictor.predict_new import predict_single
from export.result_exporter import export_prediction

import joblib
import os

def main():
    while True:
        print("\n=== LOAN DEFAULT PREDICTOR ===")
        print("1. Train model")
        print("2. Evaluasi model")
        print("3. Prediksi data baru")
        print("4. Simpan hasil prediksi")
        print("5. Keluar")
        choice = input("Pilih opsi (1/2/3/4/5): ")

        if choice == "1":
            # Load dan preprocess data
            df = load_loan_data("loan_default_project/data/loan_data.xlsx")
            X, y, scaler, emp_encoder, mar_encoder = preprocess(df)

            # Train model
            model = train_model(X, y,scaler, emp_encoder, mar_encoder)

            # Simpan model dan encoder
            joblib.dump(model, "loan_default_project/model/model.pkl")
            joblib.dump(scaler, "loan_default_project/model/scaler.pkl")
            joblib.dump(emp_encoder, "loan_default_project/model/emp_encoder.pkl")
            joblib.dump(mar_encoder, "loan_default_project/model/mar_encoder.pkl")

            print("[INFO] Model dan preprocessing tools berhasil disimpan.")

        elif choice == "2":
            if not os.path.exists("loan_default_project/model/model.pkl"):
                print("[ERROR] Belum ada model. Silakan train dulu.")
                continue

            df = load_loan_data("loan_default_project/data/loan_data.xlsx")
            X, y, scaler, emp_encoder, mar_encoder = preprocess(df)

            from sklearn.model_selection import train_test_split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            model = joblib.load("loan_default_project/model/model.pkl")
            evaluate_model(model, X_test, y_test)

        elif choice == "3":
            print("\n[INPUT] Masukkan data baru:")
            data_baru = {
                "age": int(input("Umur: ")),
                "income": float(input("Pendapatan bulanan: ")),
                "loan_amount": float(input("Jumlah pinjaman: ")),
                "loan_term_months": int(input("Lama pinjaman (bulan): ")),
                "credit_score": int(input("Skor kredit: ")),
                "employment_status": input("Status kerja (Employed/Self-employed/Unemployed): "),
                "marital_status": input("Status pernikahan (Married/Single/Divorced): ")
            }
            pred, proba = predict_single(data_baru)
            print(f"Prediksi: {'DEFAULT' if pred == 1 else 'TIDAK DEFAULT'} (Probabilitas: {proba:.2%})")

        elif choice == "4":
            save = input("Apakah ingin menyimpan hasil prediksi terakhir ke Excel? (y/n): ")
            if save.lower() == "y":
               # Tambahkan hasil prediksi ke dalam data_baru
                data_baru["prediction"] = int(pred)
                data_baru["probability"] = round(proba, 4)
    
                export_prediction(data_baru)
                print("[INFO] Hasil prediksi disimpan ke 'loan_default_project/export/prediction_result.xlsx'")

        elif choice == "5":
            print("Sampai jumpa!")
            break

        else:
            print("[ERROR] Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
