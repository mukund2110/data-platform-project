import pandas as pd

def transform_data(raw_file):
    print("Transforming data...")
    if not raw_file.endswith(".json"):
        raise ValueError("Input file must be a JSON file.")
    df = pd.read_json(raw_file)
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The JSON file does not contain a valid DataFrame.")
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    if not all(col in df.columns for col in ["userId", "id", "title"]):
        raise ValueError("The DataFrame does not contain the required columns: 'userId', 'id', 'title'.")
    df = df[["userId", "id", "title"]]
    print("Data transformed successfully.")
    return df

 