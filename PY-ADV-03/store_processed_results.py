import requests
import json

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    # Get API response
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    # Parse JSON response
    data = response.json()

    # Process the required data
    processed_data = {
        "id": data["id"],
        "user_id": data["userId"],
        "title": data["title"]
    }

    # Store processed data locally
    with open("processed_results.json", "w") as file:
        json.dump(processed_data, file, indent=4)

    print("Processed results stored successfully.")
    print("File: processed_results.json")

except requests.exceptions.RequestException as error:
    print("API Error:", error)

except (KeyError, ValueError) as error:
    print("Data processing error:", error)