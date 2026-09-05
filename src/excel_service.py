import pandas as pd

def load_excel(path: str):
  return pd.read_excel(path)

def save_excel(df, path: str):
  df.to_excel(path, index=False)

def ensure_columns(df):
  for col in ["Address","Neighborhood","City","State"]:
    if col not in df.columns:
      df[col] = ""
  return df