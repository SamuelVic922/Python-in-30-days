# Today(26/08/2025) , We are Building an app to convert a CSV to Readable format

import csv
from pathlib import Path
import os
from tabulate import tabulate

CSV_file = input("Input the file path of the CSV file: ").strip()

FILENAME = CSV_file

if not FILENAME.lower().endswith(".csv"):
    print("Error: The file must have a .csv extension.")
    exit(1)

if os.path.exists(FILENAME):
    try:
        with open(FILENAME, "r", encoding="utf-8") as csvf:
            reader = csv.DictReader(csvf)  # Reads rows as dictionaries
            rows = list(reader)  # Convert to a list for easier handling
            print(tabulate(rows[1:], headers=rows[0], tablefmt="grid"))
    except UnicodeDecodeError:
        print(
            "Error: Could not decode file with utf-8. Try another encoding like 'latin1'.")

else:
    print("Error: Issue with file path , please check file path and try again")
