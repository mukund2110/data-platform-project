import pandas as pd


def save_posts(df, processed_file):
    print("Loading data...")
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input data must be aDataFrame.")
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    df.to_csv(processed_file, index=False)
    print("Data loaded successfully.")