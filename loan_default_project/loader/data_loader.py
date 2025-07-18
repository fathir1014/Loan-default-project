import pandas as pd
import os

def load_loan_data(filepath="data/loan_data.xlsx"):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File tidak ditemukan: {filepath}")
    
    df = pd.read_excel(filepath)

    missing_count = df.isnull().sum().sum()
    if missing_count > 0:
     print(f"[WARNING] Ditemukan {missing_count} nilai kosong. Baris dengan missing values akan dihapus.")
     df = df.dropna()


    print(f"[INFO] Data berhasil dimuat. Jumlah baris: {len(df)}")
    return df
