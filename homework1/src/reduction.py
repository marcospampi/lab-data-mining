import pandas as pd
from sklearn.decomposition import PCA, TruncatedSVD

from .normalization import standardized

def compute_pca(df: pd.DataFrame, n: int = 3, std: bool = True) -> pd.DataFrame:
  df = standardized(df) if std else df
  pca = PCA(n_components=n)
  pca_fit_data = pca.fit_transform(df.values)
  pca_df = pd.DataFrame(pca_fit_data, columns=[ "principal component {0}".format(i) for i in range(n) ])

  return pca_df

def compute_svd(df: pd.DataFrame, n: int = 3, std: bool = False) -> pd.DataFrame:
  df = standardized(df) if std else df
  svd = TruncatedSVD(n_components=n)
  svd_fit_data = svd.fit_transform(df.values)
  svd_df = pd.DataFrame( svd_fit_data, columns=[ "component {0}".format(i) for i in range(n) ])

  return svd_df