import logging
import os

from api_client import get_data
from validation import validate_data
from transformation import transform_data
from storage import save_json, save_csv


# Create log file in the same folder as main.py
folder = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(folder, "application.log")


logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


try:
    print("Starting program...")
    logging.info("Program started")

    data = get_data()
    print("API data received.")
    logging.info("API data received")

    if validate_data(data):
        print("Data validation successful.")
        logging.info("Data validation successful")
    else:
        raise ValueError("Invalid data received from API.")

    processed_data = transform_data(data)
    print("Data transformation successful.")
    logging.info("Data transformation successful")

    save_json(processed_data)
    save_csv(processed_data)

    print("Data saved successfully.")
    logging.info("Data saved successfully")

    print("Processing completed successfully!")


except Exception as error:
    print("Error:", error)
    logging.error("Error occurred: %s", error)