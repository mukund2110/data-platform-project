import extract
import transform
import load
import json

def main():
    with open("config/config.json","r") as f:
        config = json.load(f)
    url = config["url"]
    raw_file = config["raw_file"]
    processed_file = config["processed_file"]
    extract.extract_data(url, raw_file)
    df = transform.transform_data(raw_file)
    load.save_posts(df, processed_file)


if __name__ == "__main__":
    main()