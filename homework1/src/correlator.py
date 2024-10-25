import numpy as np
from typing import Callable
from pandas import DataFrame
from pandas.api.types import is_numeric_dtype
from scipy.stats import pearsonr, spearmanr, kendalltau
from itertools import combinations


def pearson_fn(X: np.array, Y: np.array):
    return pearsonr(X, Y).statistic

def spearman_fn(X: np.array, Y: np.array):
    return spearmanr(X, Y).statistic

def kendall_fn(X: np.array, Y: np.array):
    return kendalltau(X, Y).statistic

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
    
    def run(self, correlationFn: Callable[[np.array, np.array], float])->dict[tuple, float]:
        return {
            (X,Y): pearson_fn(self.df[X].array, self.df[Y].array) for (X,Y) in self.column_pairs 
        }
            
        

if __name__== '__main__':
    from utils import top_dict_pairs, correlation_score_table

    from sklearn.datasets import load_wine
    df = load_wine( as_frame=True ).data
    correlator = Correlator(df)
    pearson_result = correlator.run(kendall_fn)
    print(top_dict_pairs(pearson_result, 3))
    print(correlation_score_table(pearson=top_dict_pairs(pearson_result, 3)))

