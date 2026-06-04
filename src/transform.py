import pandas as pd

df = pd.read_json("data/raw/posts.json")

df= df[["userId", "id", "title"]]

df.to_csv("data/processed/posts.csv", index=False)