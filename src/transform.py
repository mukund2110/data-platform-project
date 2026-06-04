import pandas as pd

def transform_data():
    df = pd.read_json("data/raw/posts.json")
    df = df[["userId", "id", "title"]]
    return df

