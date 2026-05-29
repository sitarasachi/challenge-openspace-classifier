import random

class Openspace:

    def __init__(self, number_of_tables, capacity_per_table):
        self.number_of_tables = number_of_tables
        self.tables = [Table(capacity_per_table) for _ in range(number_of_tables)]

    def organize(self, names):
        random.shuffle(names)
        for name in names:
            assigned = False
            for table in self.tables:
                if table.assign_seat(name):
                    assigned = True
                    break
            if not assigned:
                print(name, "could not be seated (no space left)")

    def display(self):
        for i, table in enumerate(self.tables):
            print(f"\nTable {i+1}:")
            for j, seat in enumerate(table.seats):
                status = seat.occupant if not seat.free else "Empty"
                print(f"  Seat {j+1}: {status}")

    def store(self, filename):
        with open(filename, "w") as f:
            for i, table in enumerate(self.tables):
                f.write(f"Table {i+1}:\n")
                for j, seat in enumerate(table.seats):
                    status = seat.occupant if not seat.free else "Empty"
                    f.write(f"  Seat {j+1}: {status}\n")
                f.write("\n")



