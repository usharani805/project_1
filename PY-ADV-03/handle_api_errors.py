import requests

url = "https://jsonplaceholder.typicode.com/posts/999999"

try:
    print("Connecting to API...")

    response = requests.get(url, timeout=5)

    # Handle HTTP errors
    response.raise_for_status()

    # Convert response to JSON
    data = response.json()

    print("API request successful!")
    print("ID:", data["id"])
    print("Title:", data["title"])

except requests.exceptions.Timeout:
    print("Error: The API request timed out.")

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the API.")

except requests.exceptions.HTTPError as error:
    print("HTTP Error:", error)
    print("Status Code:", response.status_code)

except requests.exceptions.RequestException as error:
    print("Request Error:", error)

except ValueError:
    print("Error: The API returned invalid JSON.")