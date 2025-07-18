import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


def preprocess(data) :

  data = data.drop(columns=["customer_id", "name"])

  if data.isnull().sum().sum() :
    verbose = False
    if verbose :
     print("[WARNING] : Ditemukan data kosong, menghapus baris yang memiliki data kosong...")
    data = data.dropna()

  emp_encoder = LabelEncoder()
  mar_encoder = LabelEncoder()
  data['employment_status'] = emp_encoder.fit_transform(data['employment_status'])
  data['marital_status'] = mar_encoder.fit_transform(data['marital_status'])

  numerical_cols = ["age", "income", "loan_amount", "loan_term_months", "credit_score"]
  scaler = StandardScaler()
  data[numerical_cols] = scaler.fit_transform(data[numerical_cols])

  X = data.drop(columns=['default'])
  y = data['default']

  return X,y, scaler, emp_encoder, mar_encoder