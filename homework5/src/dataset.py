import numpy as np
import pandas as pd


def extract_data_target(df: pd.DataFrame):
    return df.drop('class_name', axis=1).values, df['class_name'].values

def merge_prediction(test_df: pd.DataFrame, predicted: np.array):
    return pd.DataFrame(
        index=test_df.index,
        data={
            'class': test_df['class_name'],
            'predicted': predicted
        }
    )

class TrainTestSampler:
    class_column: str
    ratio: float
    df: pd.DataFrame
    seed = None
    def __init__(self, df: pd.DataFrame, class_column: str, ratio: float = .7, seed = None):
        self.df = df
        self.class_column = class_column
        self.ratio = ratio
    def _extract_sample(self, class_name: str):
        sdf = self.df[self.df[self.class_column] == class_name]
        n = int(float(sdf.shape[0]) * self.ratio )
        
        return sdf.sample(n, self.seed)
    def sample(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        class_names = list(self.df[self.class_column].drop_duplicates().values)
        train_df = pd.concat([
            self._extract_sample(class_name) for class_name in class_names
        ])
        test_df = self.df.drop(index=train_df.index)

        return (train_df, test_df)