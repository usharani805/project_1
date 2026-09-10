import requests

# REST API URL
url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    # Send GET request
    response = requests.get(url)

    # Check if request was successful
    response.raise_for_status()

    # Convert JSON response to Python dictionary
    data = response.json()

    # Display the data
    print("Post Details:")
    print("ID:", data["id"])
    print("User ID:", data["userId"])
    print("Title:", data["title"])
    print("Body:", data["body"])

except requests.exceptions.RequestException as error:
    print("Error:", error)