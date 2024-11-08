from dataclasses import dataclass
import os
import pandas as pd

from .preprocess import Preprocess



@dataclass
class Cache:
    transactions: pd.DataFrame
    categories: pd.DataFrame
    items: pd.DataFrame

    def dump(self, path: str):
        transactions_file_name, categories_file_name, items_file_name = (
            self.cached_file_names(path)
        )

        self.transactions.to_pickle(transactions_file_name)
        self.categories.to_pickle(categories_file_name)
        self.items.to_pickle(items_file_name)

    @staticmethod
    def cached_file_names(path):
        transactions_file_name = os.path.join(path, "transactions.cache.pickle")
        categories_file_name = os.path.join(path, "categories.cache.pickle")
        items_file_name = os.path.join(path, "items.cache.pickle")
        return transactions_file_name, categories_file_name, items_file_name


class CacheManager:
    _cache: Cache

    def __init__(self, source_path: str):
        if not self._try_load_cache_files(source_path):
            self._cache = self._create_cache(source_path)
            self._cache.dump(os.path.dirname(source_path))

    def _try_load_cache_files(self, source_data: str) -> bool:
        try:
            path = os.path.dirname(source_data)
            transactions_file_name, categories_file_name, items_file_name = (
                Cache.cached_file_names(path)
            )

            transactions = pd.read_pickle(transactions_file_name)
            categories = pd.read_pickle(categories_file_name)
            items = pd.read_pickle(items_file_name)

            self._cache = Cache(
                transactions=transactions, items=items, categories=categories
            )
            return True
        except FileNotFoundError:
            return False

    def get_cache(self) -> Cache:
        return self._cache

    def _create_cache(self, source_data_path):
        df = pd.read_csv(source_data_path)

        preprocess = Preprocess(df)
        transactions, items, categories = preprocess.run()

        cache = Cache(transactions=transactions, items=items, categories=categories)
        return cache

if __name__ == "__main__":
    file_path = "/home/marco/Scrivania/uni/datamining/lab-data-mining/homework2/nogit/AnonymizedFidelity.csv"
    cacheManager = CacheManager(file_path)

