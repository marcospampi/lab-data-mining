from itertools import combinations
from typing import Callable
import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr, kendalltau


def pearson_fn(X: np.array, Y: np.array):
    return pearsonr(X, Y).statistic

def spearman_fn(X: np.array, Y: np.array):
    return spearmanr(X, Y).statistic

def kendall_fn(X: np.array, Y: np.array):
    return kendalltau(X, Y).statistic

class Correlator:
    df: pd.DataFrame
    feature_pairs: list[(str,str)]
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.feature_pairs = self.__compute_feature_pairs()
        pass

    def __compute_feature_pairs(self):
        # filters pairs by types, must be numeric
        columns = [ column for column in self.df.columns if pd.api.types.is_numeric_dtype(self.df[column])]
        # create the combination set of pairs
        column_pairs = list(combinations(columns, 2))
        return column_pairs
    
    def run(self, correlationFn: Callable[[np.array, np.array], float])->dict[tuple, float]:
        return {
            (X,Y): correlationFn(self.df[X].array, self.df[Y].array) for (X,Y) in self.feature_pairs 
        }
    # merge correlation results
    def merge_correlation_results(self, **correlation_runs):
        correlation_keys = correlation_runs.keys()
        features_correlation_dict = self.compute_features_correlation_dict(correlation_runs)
        flattened_fcd_data = self.flatten_fcd_data(correlation_keys, features_correlation_dict)
        result_df = pd.DataFrame(
            data = flattened_fcd_data,
            columns = ( "Features", *correlation_keys )
        ).set_index("Features")
        
        return result_df

    def flatten_fcd_data(self, correlation_keys, features_correlation_dict):
        return [
            ( features, *[results[key] for key in correlation_keys] ) for (features, results) in features_correlation_dict.items()
        ]

    def compute_features_correlation_dict(self, correlation_runs):
        features_correlation_dict = { feature: dict() for feature in self.feature_pairs }
        for method, correlation_results in correlation_runs.items():
            for feature_pairs, value in correlation_results.items():
                features_correlation_dict[feature_pairs][method] = value
        return features_correlation_dict

