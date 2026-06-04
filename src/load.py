def save_posts(df, processed_file):
    df.to_csv(processed_file, index=False)