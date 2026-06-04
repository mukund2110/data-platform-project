import requests
import json

def extract_data(url):
    response = requests.get(url)
    data = response.json()

    with open("data/raw/posts.json", "w") as f:
        json.dump(data, f, indent=4)