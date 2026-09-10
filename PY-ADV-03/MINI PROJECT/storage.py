import json
import csv
import os


def save_json(data):
    folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(folder, "result.json")

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def save_csv(data):
    folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(folder, "result.csv")

    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["id", "title", "body"]
        )

        writer.writeheader()
        writer.writerow(data)