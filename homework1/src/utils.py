import pandas as pd
import matplotlib.pyplot as plt

def plot_feature_pairs_from_merged_set(df: pd.DataFrame, merged_set: pd.DataFrame):
    for index  in merged_set.index:
        (X,Y) = index
        plt.figure(figsize=(8,8))
        plt.title("{0} × {1}".format(X,Y))
        plt.plot(df[X].array, df[Y].array,'o')
        plt.xlabel(X)
        plt.ylabel(Y)
        plt.show()

def select_sort_n(df: pd.DataFrame, sort_by_features: list[str], n: int):
    result = (
        pd.concat([
            df.sort_values(f, ascending=False)[:n] 
            for f in sort_by_features
        ])
        .drop_duplicates()
        .assign( Mean = lambda df: df.mean(axis=1))
        .sort_values("Mean", ascending=False)

    )
    return result
