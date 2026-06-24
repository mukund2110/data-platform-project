import pandas as pd
import sys
sys.path.append("src")

import transform

def test_transform():

    # data = {
    #     'id': [1, 2, 3],
    #     'title': ['Post 1', 'Post 2', 'Post 3'],
    #     'content': ['Content 1', 'Content 2', 'Content 3']
    # }
    data = {
        "userId": [1, 2],
        "id": [101, 102],
        "title": ["A", "B"]
    }
    df = pd.DataFrame(data)
    
    df.to_json("test_data.json")

    results = transform.transform_data("test_data.json")

    assert isinstance(results, pd.DataFrame), "Output should be a DataFrame."
    assert list(results.columns) == ["userId", "id", "title"]
