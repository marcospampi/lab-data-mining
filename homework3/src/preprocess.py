import pandas as pd

interesting_columns = [
    "scontrino_id",
    "cod_prod",
    "descr_prod",
    "liv1",
    "liv2",
    "liv3",
    "liv4",
    "descr_liv1",
    "descr_liv2",
    "descr_liv3",
    "descr_liv4",
]

transaction_columns = ["scontrino_id", "cod_prod"]

category_columns = ["id", "descr"]
item_columns = ["cod_prod", "descr_prod", "liv1", "liv2", "liv3", "liv4"]


class Preprocess:
    df: pd.DataFrame
    wk: pd.DataFrame

    def __init__(self, df: pd.DataFrame):
        self.df = df
        pass

    def _select(self):
        self.df = self.df[interesting_columns]

    def _normalize(self):
        self.df =(
            self.df
                .dropna()
                .astype(
                    {
                        "scontrino_id": "int64",
                        "cod_prod": "int64",
                        "liv1": "int64",
                        "liv2": "int64",
                        "liv3": "int64",
                        "liv4": "int64",
                    }
                )
        )
    def _extract_items(self):
        items = (
            self.df[item_columns]
            .drop_duplicates()
            .set_index(["cod_prod"])
        )
        items['descr_prod'] = items['descr_prod'].map( lambda descr: descr[7:].strip())
        return items

    def _extract_transactions(self):
        return self.df[transaction_columns].drop_duplicates().set_index(["scontrino_id"])

    def _extract_categories(self) -> pd.DataFrame:

        def extract_level(df: pd.DataFrame, n: int) -> pd.DataFrame:
            extract_columns = [f"liv{n}", f"descr_liv{n}"]
            rename_columns = dict(zip(extract_columns, category_columns))
            df = df[extract_columns].rename(columns=rename_columns)
            return df

        result = (
            pd.concat([extract_level(self.df, n + 1) for n in range(0, 4)])
            .drop_duplicates()
            .set_index(["id"])
        )
        return result
    def run(self) -> tuple[pd.DataFrame,pd.DataFrame,pd.DataFrame]:
        self._select()
        self._normalize()

        transactions = self._extract_transactions()
        items = self._extract_items()
        categories = self._extract_categories()

        return transactions, items, categories