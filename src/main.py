import extract
import transform
import load

def main():
    url = "https://jsonplaceholder.typicode.com/posts"
    extract.extract_data(url)
    df = transform.transform_data()
    load.save_posts(df)


if __name__ == "__main__":
    main()