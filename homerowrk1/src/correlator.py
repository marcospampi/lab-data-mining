from typing import Callable
from pandas import DataFrame
from pandas.api.types import is_numeric_dtype
from scipy.stats import pearsonr, spearmanr, kendalltau
from itertools import combinations


def pearson_fn(columns: tuple[str, str], df: DataFrame):
    X, Y = df[columns[0]], df[columns[1]]
    return pearsonr(X.array, Y.array).statistic

def spearman_fn(columns: tuple[str, str], df: DataFrame):
    X, Y = df[columns[0]], df[columns[1]]
    return spearmanr(X.array, Y.array).statistic

def kendall_fn(columns: tuple[str, str], df: DataFrame):
    X, Y = df[columns[0]], df[columns[1]]
    return kendalltau(X.array, Y.array).statistic

class Correlator:
    df: DataFrame
    column_pairs: list[(str,str)]
    def __init__(self, df: DataFrame):
        self.df = df
        self.column_pairs = self.__compute_feature_pairs()
        pass

    def __compute_feature_pairs(self):
        # filters pairs by types, must be numeric
        columns = [ column for column in self.df.columns if is_numeric_dtype(self.df[column])]
        # create the combination set of pairs
        column_pairs = list(combinations(columns, 2))
        return column_pairs
    
    def run(self, correlationFn: Callable[[tuple[str, str],DataFrame], float])->dict[tuple, float]:
        return {
            pairs: pearson_fn(pairs, self.df) for pairs in self.column_pairs 
        }
            
        

if __name__== '__main__':
    from utils import top_dict_pairs

    from sklearn.datasets import load_wine
    df = load_wine( as_frame=True ).data
    correlator = Correlator(df)
    pearson_result = correlator.run(kendall_fn)
    print(top_dict_pairs(pearson_result, 3))

