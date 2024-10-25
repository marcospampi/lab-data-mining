import pandas as pd
import matplotlib.pyplot as plt

from IPython.display import Markdown, display
def printmd(string):
    display(Markdown(string))

def top_dict_pairs(src: dict, count: int) -> dict:
    return {
        key: value  for key, value in list(sorted(src.items(), key = lambda tup: tup[1], reverse=True ))[:count]
    }

def correlation_score_table(**kwargs):
    ds = [
        (key, columns, correlation) for key, value in kwargs.items() for (columns, correlation) in value.items()
    ]
    df = pd.DataFrame.from_records(ds, columns=('Correlation name','Features',' Correlation'))
    return df

def plot_correlations(df: pd.DataFrame, **kwargs):
    for correlation, feature_pairs in kwargs.items():
        printmd("#### {0}".format(correlation) )
        for (X,Y) in feature_pairs:
            plt.title("Features {0} e {1}:".format(X,Y))
            plt.plot(df[X].array, df[Y].array,'o')
            plt.xlabel(X)
            plt.ylabel(Y)
            plt.show()
    
