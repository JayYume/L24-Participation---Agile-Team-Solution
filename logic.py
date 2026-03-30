import pandas as pd

def calculate_stats(df):
    if(df.empty):
        return 0, 0, 0
    else:
        average = df["Grade"].mean()
        high = df["Grade"].max()
        low = df["Grade"].min()
        return average, high, low

def get_grade_bins(df):
    if(df.empty):
        return pd.Series(dtype=int)
    else:
        bins = [0, 60, 70, 80, 90]
        labels = ['F', 'D', 'C', 'B', 'A']
        return pd.cut(df['Grade'], bins=bins, labels=labels).value_counts().sort_index()