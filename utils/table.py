class Seat:

     
    def __init__(self):
        """The constructor initializes the Seat object with an occupant 
          and a free status.The seat starts out empty
        occupant = " " means no one is sitting there
        free = True means the seat is available"""
        self.occupant = " "
        self.free = True
        

    def set_occupant(self,name):
      # if the seat is free, we need to assign an occupant  
        """The set_occupant method tries to put someone on the seat
        If the seat is free, The person is assigned to the seat
        Then the seat becomes occupied A message is printed confirming the assigning of 
        the occupant to the seat.If the seat is already occupied, it prints a message indicating
        that the seat is not free."""
        if self.free:
            self.occupant = name
            self.free = False
            
            print("The seat is now occupied by " + name)
            
        else:
            print("The seat is not free")
            
        


    def remove_occupant(self):
        """The remove_occupant method removes the person sitting in the seat.If someone is sitting,
        it remembers their name , clears the seat and marks it as free again and prints the seat status
        is free and was occupied by with the old person name, also returns the 
        name of the person(old_name) who left. If the seat is already free, it prints a message indicating 
        that the seat is already free and returns None."""
        
        if not self.free:
            old_name = self.occupant
            self.occupant = " "
            self.free = True

            print("The seat is free and was occupied by " + old_name)
            return old_name

        else:
            print("The seat is already free")
            return None
        
        





class Table:
       
    def __init__(self, capacity):
        """The constructor initializes the Table object with a specified capacity and creates
        a list of Seat objects based on that capacity. Each seat is initialized as free with a space 
        as the occupant."""
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]

        


    def has_free_spot(self):
        """The has_free_spot method checks if there is at least one free seat on the table.
        It iterates through all seats and returns True if any seat is free, otherwise False."""
        for seat in self.seats:
            if seat.free:
                
                return True
        return False
    
        

    def assign_seat(self, name):
        """The assign_seat method tries to assign a person
        to a free seat at the table. It iterates through the seats, and if it finds
        a free seat, it uses the set_occupant method to assign the person to that seat."""
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        print("No free seats available")
        return False
    
        
        
    
    def left_capacity(self):
        """The left_capacity method counts how many free seats are left at the table.
        It iterates through the seats and counts how many are free, then prints and 
        returns that count."""
        count = 0
        for seat in self.seats:
            if seat.free:
                count += 1
        print(f"There are {count} seats left")
        return count





def _str__(self):
    """The __str__ method provides a string representation of the Table object. It constructs a string that lists the status of each seat at the table, indicating whether it is occupied and by whom, or if it is empty."""
    result = f"Table with capacity {self.capacity}:\n"
    for i, seat in enumerate(self.seats):
        status = seat.occupant if not seat.free else "Empty"
        result += f"  Seat {i+1}: {status}\n"
    return result
