import requests
import json

def extract_data(url, raw_file):
    print("Extracting data...")
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, list):
        raise ValueError("The API response is not a list of posts.")
    with open(raw_file, "w") as f:
        json.dump(data, f, indent=4)
    print("Data extracted successfully.")
    return data