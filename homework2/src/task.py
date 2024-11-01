import os
import pandas as pd

cached_columns = [
    'scontrino_id',
    'cod_prod',
    'descr_prod',
    'liv1',
    'descr_liv1',
    'liv2',
    'descr_liv2',
    'liv3',
    'descr_liv3',
    'liv4',
    'descr_liv4'
]

class Task:
    cached_norm: pd.DataFrame
    def __init__(self):
        
        pass
    def create_cached_norm(self) -> pd.DataFrame:
        original_file_path = os.path.join(os.path.abspath(''),'..','tmp','AnonymizedFidelity.csv')
        original_df = pd.read_csv(original_file_path)
        cached_df = original_df[cached_columns]

