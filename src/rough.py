import requests
import json
import pandas as pd
# url = "https://jsonplaceholder.typicode.com/posts"

# response = requests.get(url)

# print(response.status_code)

# print(response.json()[:2])

# print(type(response))

# print(type(response.json()))

# data = response.json()
# with open("data/raw/posts.json", "w") as f:
#     json.dump(data, f, indent=4)

# print(type(response))
# print(type(data))
# print(len(data))

df = pd.read_json("config/config.json")
print(df["url"][0])