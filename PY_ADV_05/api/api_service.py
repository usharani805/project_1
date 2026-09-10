import requests


def get_api_data():
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()