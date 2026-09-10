import pandas as pd
import sys
import pytest
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
    assert len(results)== 2, "dataframe should have 2 rows."

def test_missing_columns():
    data = {
        "userId": [1, 2],
        "id": [101, 102],
    }
    df = pd.DataFrame(data)
    df.to_json("test_data.json")

    with pytest.raises(ValueError):
        transform.transform_data("test_data.json")

def test_empty_dataframe():

    data ={}
    df = pd.DataFrame(data)
    df.to_json("test_data.json")
    with pytest.raises(ValueError):
        transform.transform_data("test_data.json")
    # data ={        
    #     "userId": [],
    #     "id": [],
    #     "title": []
    # }
    df = pd.DataFrame(data)
    df.to_json("test_data.json")
    with pytest.raises(ValueError):
        transform.transform_data("test_data.json")
def test_invalid_file_extension():
    data = {
        "userId": [1, 2],
        "id": [101, 102],
    }
    df = pd.DataFrame(data)
    df.to_csv("test_data.csv")
    with pytest.raises(ValueError):
        transform.transform_data("test_data.csv")
def test_whelther_transform_works_as_expected():
    data = {
        "userId": [1, 2],
        "id": [101, 102],
        "title": ["A", "B"],
        "comment": ["commentA", "commentB"]
    }
    df = pd.DataFrame(data)
    df.to_json("test_data.json")

    assert transform.transform_data("test_data.json").equals(df[["userId", "id", "title"]]), "The transformed DataFrame does not match the expected output."
def test_required_columns():
    data = {
        "userId": [1, 2],
        "id": [101, 102]
    }
    df = pd.DataFrame(data)
    df.to_json("test_data.json")

    with pytest.raises(ValueError):
        transform.transform_data("test_data.json")
def test_empty_data(tmp_path):
    test_file = tmp_path / "test_data.json"
    data ={        
        "userId": [],
        "id": [],
        "title": []
    }
    df = pd.DataFrame(data)
    df.to_json(test_file)
    with pytest.raises(ValueError):
        transform.transform_data(test_file)
def test_transform_works_expected(tmp_path):
    test_file = tmp_path / "test_data.json"
    data = {
        "userId": [1, 2],
        "id": [101, 102],
        "title": ["A", "B"],
        "comment": ["commentA", "commentB"]
    }
    df = pd.DataFrame(data)
    df.to_json(test_file)
    expected_df = df[["userId", "id", "title"]]
    result_df = transform.transform_data(test_file)
    assert result_df.equals(expected_df), "The transformed DataFrame does not match the expected output."
