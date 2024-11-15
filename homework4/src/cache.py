from typing import Callable, Self
import pandas as pd


class CachedDataFrame:
    path: str
    df: pd.DataFrame
    def __init__(self, path: str):
        self.path = path
    
    def load(self) -> Self:
        self.df = pd.read_pickle(self.path)
        return self
    
    def store(self) -> Self:
        self.df.to_pickle(self.path)
        return self
    
    def get(self) -> pd.DataFrame:
        return self.df
    
    def set(self, df: pd.DataFrame) -> Self:
        self.df = df
        return self

def cache_factory(path: str, *, df_factory: Callable[[],pd.DataFrame] ) -> CachedDataFrame:
    try:
        return CachedDataFrame(path).load()
    except FileNotFoundError:
        return CachedDataFrame(path).set(df_factory()).store()