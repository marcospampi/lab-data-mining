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
