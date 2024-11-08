import pandas as pd

def item_cross_trx(trx_df: pd.DataFrame, *, min_support = 0.2) -> pd.DataFrame:
    supported_trx_df = extract_min_support(trx_df, min_support)
    
    cross_trx_df = (
        pd.crosstab(supported_trx_df.index, supported_trx_df['cod_prod'])
        .astype('bool')
    )
    return cross_trx_df

def extract_min_support(trx_df, min_support):
    supported_ss = (
        trx_df['cod_prod']
            .value_counts(normalize=True)
    )
    supported_ss = supported_ss[supported_ss > min_support ]
    supported_trx_df = trx_df[trx_df['cod_prod'].isin(supported_ss.index)]
    return supported_trx_df



