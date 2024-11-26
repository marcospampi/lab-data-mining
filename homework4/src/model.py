from typing import Literal, Optional, Sequence, Union
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import StandardScaler
from sklearn.metrics import silhouette_score

class ModelFamily:
    pca_n_components: Optional[int] = None
    range: Sequence[int] = range(0)
    init: Union[Literal['k-means++'], Literal['random']] = 'k-means++'
    max_iter: Optional[int] = 300
    df: pd.DataFrame
    seed: int = np.random.randint(0,2**24)

    pca_df: Optional[pd.DataFrame]

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def with_pca(self, pca: Optional[int]):
        self.pca_n_components = pca
        self.pca_df = None
        return self
    
    def with_range(self, range: Sequence[int]):
        self.range = range
        return self
    def with_seed(self, seed: int):
        self.seed = seed
        return self
    
    def with_init(self, init: Union[Literal['k-means++'], Literal['random']] = 'k-means++'):
        self.init = init
        return self
    
    def with_max_iter(self, max_iter: Optional[int]):
        self.max_iter = max_iter
        return self
    
    def evaluate_k(self, k: int):
        df = self.get_df()
        return KMeans(k, init = self.init, max_iter=self.max_iter, random_state=self.seed).fit(df)
    
    def labels_k(self, k: int):
        df = self.get_df()
        labels_df = pd.Series(
            data=self.evaluate_k(k).predict(df), 
            index=self.df.index
        )
        return labels_df
    
    def _evaluate_pca(self):
        scaled_df = StandardScaler().fit_transform(self.df)
        self.pca_df = pd.DataFrame(
            data=PCA(n_components = self.pca_n_components ).fit_transform(scaled_df), 
            columns=[f'pca {i}' for i in range(self.pca_n_components)],
            index=self.df.index
        )
        return self
    
    def get_df(self) -> pd.DataFrame:
        if self.pca_n_components is not None:
            if self.pca_df is None:
                self._evaluate_pca()
            return self.pca_df
        else:
            return self.df



class ModelFamilyEvaluator:
    families: dict[str, ModelFamily] = dict()
    cache: dict[str, ]
    def __init__(self):
        pass
    def add_family(self, name: str, family: ModelFamily):
        self.families[name] = family
        return self
    
    def remove_family(self, name: str):
        del self.families[name]
        return self
    
    def plot_elbow(self):
        families_count = len(self.families)

        plot_rows = int(np.ceil(families_count / 2))
        fig, axes = plt.subplots(nrows=plot_rows, ncols=2, figsize=(9, 4*plot_rows))
        for idx, (name, family) in enumerate(self.families.items()):
            i,j = int(idx / 2), idx % 2
            ax = axes[i,j] if families_count > 2 else axes[j] 

            ax.set_title(name)
            elbow = [family.evaluate_k(n).inertia_ for n in family.range ]
            ax.plot(family.range, elbow, '-o')
            
            ax.set_ylabel('Inertia')
            ax.set_xlabel('Number of clusters')
            
            ax.grid(True)
            
        plt.suptitle('Elbow Method', fontsize=16)
        plt.tight_layout()
        plt.show()
    
    def silhouette(self, families_ranges_dict: dict[str, Sequence[int]]):
        seq = [ (name, n) for name, sequence in families_ranges_dict.items() for n in sequence ]
        scores = []
        for (name, n) in seq:

            family = self.families[name]
            labels = family.labels_k(n)
            
            df = family.get_df()
            score = silhouette_score(df, labels)
            scores.append(score)
           
        return pd.DataFrame(
            data =[ (*seq[n],scores[n]) for n in range(len(seq))],
            columns=('model', 'clusters', 'score')
        ).sort_values('score', ascending=False)
    
    def extract_labels(self, family: str, n_clusters: int) -> pd.Series:
        return self.families[family].labels_k(n_clusters)


