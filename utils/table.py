"""__init__() (the constructor)"""

class Seat:

  
    
    def __init__(self):
        self.occupant = " "
        self.free = True
        """The constructor initializes the Seat object with an occupant 
          and a free status.The seat starts out empty
        occupant = " " means no one is sitting there
        free = True means the seat is available"""

    def set_occupant(self,name):
      # if the seat is free, we need to assign an occupant  
        if self.free:
            self.occupant = name
            self.free = False
            
            print("The seat is now occupied by " + name)
            
        else:
            print("The seat is not free")
            
        """The set_occupant method tries to put someone on the seat
        If the seat is free, The person is assigned to the seat
        Then the seat becomes occupied A message is printed confirming the assigning of 
        the occupant to the seat.If the seat is already occupied, it prints a message indicating
        that the seat is not free."""


    def remove_occupant(self):
        if not self.free:
            old_name = self.occupant
            self.occupant = " "
            self.free = True

            print("The seat is free and was occupied by " + old_name)
            return old_name

        else:
            print("The seat is already free")
            return None
        
        """The remove_occupant method removes the person sitting in the seat.If someone is sitting,
        it remembers their name , clears the seat and marks it as free again and also returns the 
        name of the person who left. If the seat is already free, it prints a message indicating 
        that the seat is already free and returns None."""





class Table:
       
    def __init__(self, capacity):
        self.capacity = capacity
        self.seats = [Seat(True, " ") for _ in range(capacity)]

        """The constructor initializes the Table object with a specified capacity and creates
        a list of Seat objects based on that capacity. Each seat is initialized as free with a space 
        as the occupant."""


    def has_free_spot(self):
        for seat in self.seats:
            if seat.free:
                
                return True
        return False
    
        """The has_free_spot method checks if there is at least one free seat on the table.
        It iterates through all seats and returns True if any seat is free, otherwise False."""

    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                print("Assigned", name, "to a seat at this table")
                return True
        print("No free seats available")
        return False
    
    def left_capacity(self):
        count = 0
        for seat in self.seats:
            if seat.free:
                count += 1
        print(f"There are {count} seats left")
        return count






t = Table(6)
t.has_free_spot()
t.assign_seat("Sitara")
t.assign_seat("Neha")
t.left_capacity()            