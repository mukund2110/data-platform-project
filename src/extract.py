import requests
import json

def extract_data(url, raw_file):
    response = requests.get(url)
    data = response.json()

    with open(raw_file, "w") as f:
        json.dump(data, f, indent=4)
    return data