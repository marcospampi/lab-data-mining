import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

def to_sparse(trx_df: pd.DataFrame) -> pd.DataFrame:
    trx_ss = _create_trx_series(trx_df)

    df = _fit_and_transform_sparse(trx_ss)

    return df

def _fit_and_transform_sparse(trx_ss):
    te = TransactionEncoder()
    te_ary = te.fit(trx_ss).transform(trx_ss)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    return df

def _create_trx_series(trx_df):
    trx_ss = (
        trx_df
            .groupby(by=['scontrino_id'])[trx_df.columns[0]]
            .agg(frozenset)
    )

    return trx_ss

def resolve_descriptions(rules_df: pd.DataFrame, categories_df: pd.DataFrame) -> pd.DataFrame:
    extract = lambda e: ', '.join(categories_df['descr'].loc[e])
    return rules_df['antecedents'].map( extract ) + ' => ' + rules_df['consequents'].map(extract)


