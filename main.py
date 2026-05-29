import csv

with open("new_colleagues.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

