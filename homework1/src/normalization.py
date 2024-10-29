import pandas as pd
from sklearn.preprocessing import StandardScaler

def standardized(df: pd.DataFrame):
  scaler = StandardScaler()
  return pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
