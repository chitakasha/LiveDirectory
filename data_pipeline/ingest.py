import os
import json

def ingest_data(data_file):
    """Ingests data from a JSON file into the database."""

    with open(data_file, "r") as f:
        data = json.load(f)

    # Connect to the database
    connection = sqlite3.connect("data/chitakasha.db")
    cursor = connection.cursor()

    # Insert the data into the database
    for row in data:
        cursor.execute("INSERT INTO entries (text) VALUES (?)", (row["text"],))

    # Commit the changes to the database
    connection.commit()

    # Close the connection to the database
    connection.close()

def main():
    """The main function of the ingest script."""

    # Get the data file path
    data_file_path = os.path.join("data", "data.json")

    # Ingest the data
    ingest_data(data_file_path)

if __name__ == "__main__":
    main()

