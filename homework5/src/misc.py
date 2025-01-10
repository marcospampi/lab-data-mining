import pandas as pd

class_colors = {'ASD':'red','GDD': 'green', 'Controlli': 'blue'}
df_dtypes = {
    "Paziente": pd.Int32Dtype(),
    "Sesso": pd.CategoricalDtype(['F','M']),
    "Età equivalente": pd.Int8Dtype(),
    "B1": pd.Int8Dtype(),
    "B6": pd.Int8Dtype(),
    "B10": pd.Int8Dtype(),
    "B11": pd.Int8Dtype(),
    "B13": pd.Int8Dtype(),
    "B14": pd.Int8Dtype(),
    "B16": pd.Int8Dtype(),
    "B2": pd.Int8Dtype(),
    "B3": pd.Int8Dtype(),
    "B9": pd.Int8Dtype(),
    "B10": pd.Int8Dtype(),
    "B13": pd.Int8Dtype(),
    "B14": pd.Int8Dtype(),
    "D3": pd.Int8Dtype(),
    "D4": pd.Int8Dtype(),
    "D13": pd.Int8Dtype(),
    "D14": pd.Int8Dtype(),
    "D15": pd.Int8Dtype(),
    "D16": pd.Int8Dtype(),
    "D18": pd.Int8Dtype(),
    "D2": pd.Int8Dtype(),
    "D3": pd.Int8Dtype(),
    "D4": pd.Int8Dtype(),
    "D7": pd.Int8Dtype(),
    "D8": pd.Int8Dtype(),
    "D9": pd.Int8Dtype(),
    "D10": pd.Int8Dtype(),
    "D13": pd.Int8Dtype(),
    "D14": pd.Int8Dtype(),
    "D15": pd.Int8Dtype(),
    "D1": pd.Int8Dtype(),
    "D2": pd.Int8Dtype(),
    "D4": pd.Int8Dtype(),
    "D5": pd.Int8Dtype(),
    "D7": pd.Int8Dtype(),
    "D8": pd.Int8Dtype(),

}

class_names = ['ASD','GDD', 'Controlli']

noisy_features = ['Età cronologica (mesi)', "Scala B", "Scala D", "TOT.", "Score di rischio"]