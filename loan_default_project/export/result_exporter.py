import pandas as pd
import os

def export_prediction(metrics: dict, filepath="loan_default_project/export/evaluation_report.xlsx"):
    # Pastikan folder tujuan ada
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Ubah dict jadi DataFrame satu baris
    df = pd.DataFrame([metrics])

    # Simpan ke Excel
    df.to_excel(filepath, index=False)
    print(f"[INFO] Hasil evaluasi disimpan di {filepath}")
