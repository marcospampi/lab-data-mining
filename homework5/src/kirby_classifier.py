from sklearn.base import BaseEstimator
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import StandardScaler
from sklearn.pipeline import Pipeline


class KirbyClassifier(BaseEstimator):
    _params: dict = {}
    _pipeline: Pipeline

    def __init__(self, **params):
        self._params = params
    
    def _build_pipeline(self):
        params = self._params
        pipeline_list = []
        
        # do we need PCA?
        if 'PCA' in params and params['PCA'] > 0:
            pipeline_list.append(('standard_scaler',StandardScaler()))
            pipeline_list.append(('PCA', PCA(n_components=int(params['PCA']))))
        
        # configure and register our classifier to the pipeline
        classifier: BaseEstimator = params['classifier']
        classifier_params = { key: value for (key, value) in params.items() or {} if key not in ['PCA','classifier']}
        classifier.set_params(**classifier_params)
        pipeline_list.append(('classifier',classifier))

        self._pipeline = Pipeline(pipeline_list)

    def fit(self,X, y, **params):
        self._build_pipeline()
        self._pipeline.fit(X, y,**params)
        return self
    
    def score(self, X, y, sample_weight=None):
        return self._pipeline.score(X,y, sample_weight)
    
    def predict(self,X):
        return self._pipeline.predict(X)
    
    def get_params(self, deep: bool):
        return self._params
    
    def set_params(self, **params):
        self._params = params
        return self