def save_posts(df):
    df.to_csv("data/processed/posts.csv", index=False)