import csv
def read_names_from_csv(filepath: str) -> list:

    """Reads names from a CSV file and returns them as a list.
        The function takes the file path as an argument, opens the file,
        and uses the csv.reader to read the contents. It iterates 
        through each row in the CSV, checks if the row is not empty, and appends"""
    names = []
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Ensure the row is not empty
                names.append(row[0])  # Assuming names are in the first column
    return names

