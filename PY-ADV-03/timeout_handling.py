import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    print("Sending request to API...")

    # Wait for a maximum of 5 seconds
    response = requests.get(url, timeout=5)

    response.raise_for_status()

    data = response.json()

    print("Request successful!")
    print("Post ID:", data["id"])
    print("Title:", data["title"])

except requests.exceptions.Timeout:
    print("Error: The API request took too long.")

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the API.")

except requests.exceptions.RequestException as error:
    print("API Error:", error)