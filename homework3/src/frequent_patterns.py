from typing import Literal
import pandas as pd
from abc import ABC, abstractmethod
from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules

class FrequentItemsets:
    df: pd.DataFrame
    name: str
    def __init__(self, df: pd.DataFrame):
        self.df = df
    
    def compare(self, other) -> pd.DataFrame:
        result = (
            self.df
            .merge(other.df, how='outer', on='itemsets')
            .reindex()
        )       
        return FrequentItemsets(result[['itemsets', 'support_x', 'support_y']])

    def extract_rules(self,*, metric = 'confidence', min_threshold=.7, support_by: Literal['left', 'right'] = 'left') -> pd.DataFrame:
        tmp_df = self.df
        if not 'support' in self.df.columns:
            support_col_name = 'support_x' if support_by == 'left' else 'support_y'
            tmp_df = tmp_df[['itemsets', support_col_name ]].rename(columns={support_col_name: 'support'})
        
        rules_df = association_rules(tmp_df, metric=metric, min_threshold=min_threshold)
        return rules_df

class FrequentPatternAlgorithm(ABC):
    df: pd.DataFrame
    def __init__(self, df: pd.DataFrame):
        self.df = df

    @abstractmethod
    def run(self, min_support = 0.2) -> FrequentItemsets:
        pass


class AprioriAlgorithm(FrequentPatternAlgorithm):
   low_memory = False
   def run(self, min_support = 0.2) -> FrequentItemsets:
        result = apriori(self.df, min_support=min_support, low_memory=self.low_memory, use_colnames=True)
        return FrequentItemsets(result)

class AprioriLowMemAlgorithm(AprioriAlgorithm):
   low_memory = True

class FpGrowthAlgorithm(FrequentPatternAlgorithm):
   def run(self, min_support = 0.2) -> FrequentItemsets:
        result = fpgrowth(self.df, min_support=min_support, use_colnames=True)
        return FrequentItemsets(result)
