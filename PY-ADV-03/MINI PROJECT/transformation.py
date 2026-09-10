def transform_data(data):

    processed_data = {
        "id": data["id"],
        "title": data["title"].upper(),
        "body": data["body"]
    }

    return processed_data