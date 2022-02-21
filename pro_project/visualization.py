import pandas as pd


def show_corr(df, feature_target):
    return df.corr()[[feature_target]].applymap(lambda x: abs(x)).sort_values(feature_target, ascending=False)
    

