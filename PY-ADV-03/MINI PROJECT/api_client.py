import requests


def get_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url, timeout=5)

    response.raise_for_status()

    return response.json()