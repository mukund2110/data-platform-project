import pandas as pd

def transform_data(raw_file):
    df = pd.read_json(raw_file)
    df = df[["userId", "id", "title"]]
    return df

