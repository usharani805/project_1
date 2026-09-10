import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    # Parse JSON response
    data = response.json()

    # Extract required values
    post_id = data["id"]
    user_id = data["userId"]
    title = data["title"]
    body = data["body"]

    print("API Response Parsed Successfully")
    print("Post ID:", post_id)
    print("User ID:", user_id)
    print("Title:", title)
    print("Body:", body)

except requests.exceptions.RequestException as error:
    print("API Error:", error)

except ValueError:
    print("Error: Invalid JSON response.")