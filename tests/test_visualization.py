from pro_project.visualization import show_corr
import pandas as pd
import seaborn as sns

def test_type_show_corr():
    df = sns.load_dataset("iris")
    
    assert type(show_corr(df, "petal_width")) == pd.core.frame.DataFrame
