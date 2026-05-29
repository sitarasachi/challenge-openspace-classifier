import random
from utils.table import Table


class Openspace:

    def __init__(self):
        """The constructor initializes the Openspace object with a fixed number
        of tables and seats per table. It creates a list of tables, where each table is an 
        instance of the Table class with a specified capacity. The number of tables and 
        seats per table are set to 6 and 4 respectively, as per the requirement."""
        # FIXED REQUIREMENT: 6 tables of 4 seats
        self.number_of_tables = 6
        self.seats_per_table = 4
        self.tables = [Table(self.seats_per_table) for _ in range(self.number_of_tables)]


    def organize(self, names):
        """The organize method takes a list of names and tries to assign each name to a seat at
        the tables. It shuffles the list of names to ensure random seating and then iterates through
        each name, trying to assign it to a free seat at any of the tables. IFf a name cannot be
        assigned because there are no free seats left, it prints a message indicating that the person
        could not be seated due to lack of space."""
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
        """The display method prints the current seating arrangement of the tables. It iterates through
        each table and each seat within the table, printing the occupant of each seat or indicating if the
        seat is empty."""
        for i, table in enumerate(self.tables):
            print(f"\nTable {i+1}:")
            for j, seat in enumerate(table.seats):
                status = seat.occupant if not seat.free else "Empty"
                print(f"  Seat {j+1}: {status}")

    def store(self, filename):
        """The store method saves the current seating arrangement to a csv file. It iterates through
        each table and each seat within the table, writing the occupant of each seat or indicating if the
        seat is empty. The output is formatted to show the table number and the status of each seat. 
        The filename is provided as an argument to the method."""
        with open(filename, "w") as f:
            for i, table in enumerate(self.tables):
                f.write(f"Table {i+1}:\n")
                for j, seat in enumerate(table.seats):
                    status = seat.occupant if not seat.free else "Empty"
                    f.write(f"  Seat {j+1}: {status}\n")
                f.write("\n")

def _str_(self):
    """The __str__ method provides a string representation of the Openspace object. It constructs a string that lists the status of each table and seat."""
    result = "Openspace:\n"
    for i, table in enumerate(self.tables):
        result += f"  Table {i+1}:\n"
        for j, seat in enumerate(table.seats):
            status = seat.occupant if not seat.free else "Empty"
            result += f"    Seat {j+1}: {status}\n"
    return result
