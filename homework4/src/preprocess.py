
from abc import ABC, abstractmethod

import pandas as pd

interesting_columns = {
    "scontrino_id": 'int64',
    "tessera": 'int64',
    "cod_prod": 'int64',
    "descr_prod": 'str',
    "liv1": 'int64',
    "liv2": 'int64',
    "liv3": 'int64',
    "liv4": 'int64',
    "descr_liv1": 'str',
    "descr_liv2": 'str',
    "descr_liv3": 'str',
    "descr_liv4": 'str',
}

transaction_columns = ["scontrino_id","tessera","cod_prod"]
category_columns = ["id", "descr"]
item_columns = ["cod_prod", "descr_prod", "liv1", "liv2", "liv3", "liv4"]


class Preprocess(ABC):
    df: pd.DataFrame
    def __init__(self, df: pd.DataFrame):
        self.df = df
    
    @abstractmethod
    def run(self) -> pd.DataFrame:
        return self.df



class PreprocessItems(Preprocess):
    def run(self) -> pd.DataFrame:
        items = (
            self.df[item_columns]
                .drop_duplicates()
                .set_index(["cod_prod"])
        )
        items['descr_prod'] = items['descr_prod'].map( lambda descr: descr[7:].strip())
        return items

class PreprocessTransactions(Preprocess):
    def run(self) -> pd.DataFrame:
        return (
            self.df[transaction_columns]
                .drop_duplicates()
                .dropna()
                .astype({'tessera': 'int64', 'cod_prod': 'int64'})
                .set_index(["scontrino_id"])
        )

class PreprocessCategories(Preprocess):
    def _extract_level(self, n: int):
        extract_columns = [f"liv{n}", f"descr_liv{n}"]
        rename_columns = dict(zip(extract_columns, category_columns))
        df = self.df[extract_columns].rename(columns=rename_columns)
        return df

    def run(self) -> pd.DataFrame:
        result = (
            pd.concat([self._extract_level(self.df, n + 1) for n in range(0, 4)])
            .drop_duplicates()
            .set_index(["id"])
        )
        return result
    
class PreprocessItemCustomerFrequencyMatrix(Preprocess):
    def run(self) -> pd.DataFrame:
        trx_df = PreprocessTransactions(self.df).run()
        return pd.crosstab(trx_df['tessera'], trx_df['cod_prod'])

if __name__ == '__main__':
    src_df = pd.read_csv("/home/marco/Scrivania/uni/datamining/lab-data-mining/nogit/AnonymizedFidelity.csv")
    crosstab = PreprocessItemCustomerFrequencyMatrix(src_df).run()
    print(crosstab)