from typing import Literal
import pandas as pd
from abc import ABC, abstractmethod
from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules

class FrequentItemsets:
    df: pd.DataFrame
    name: str
    def __init__(self, name: str, df: pd.DataFrame):
        self.name = name
        self.df = df
        self.df[name] = True
    
    def compare(self, other) -> pd.DataFrame:
        result = (
            self.df
            .merge(other.df, how='outer', on='itemsets')
            .reindex()
        )
        result[other.name] = result[other.name].fillna(False)
        result[self.name] = result[self.name].fillna(False)

        result = result.rename(columns= {
            'support_x': f'support_{self.name}',
            'support_y': f'support_{other.name}'
        })
        
        return result

    def extract_rules(self,*, metric = 'confidence', min_threshold=.7) -> pd.DataFrame:
        rules_df = association_rules(self.df, metric=metric, min_threshold=min_threshold)
        return rules_df

class FrequentPatternAlgorithm(ABC):
    df: pd.DataFrame
    def __init__(self, df: pd.DataFrame):
        self.df = df

    @abstractmethod
    def run(self, min_support = 0.2) -> FrequentItemsets:
        pass


class AprioriAlgorithm(FrequentPatternAlgorithm):
   def run(self, min_support = 0.2) -> FrequentItemsets:
        result = apriori(self.df, min_support=min_support, low_memory=True, use_colnames=True)
        return FrequentItemsets('apriori',result)

class FpGrowthAlgorithm(FrequentPatternAlgorithm):
   def run(self, min_support = 0.2) -> FrequentItemsets:
        result = fpgrowth(self.df, min_support=min_support, use_colnames=True)
        return FrequentItemsets('fpgrowth',result)
