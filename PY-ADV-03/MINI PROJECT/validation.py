def validate_data(data):

    if "id" not in data:
        return False

    if "title" not in data:
        return False

    if "body" not in data:
        return False

    return True