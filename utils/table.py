class Seat:
    
    def __init__(self,free = True,occupant= " "):
        self.occupant = str(occupant)
        self.free = free
        if self.occupant == " ":
            self.free = True
        else:
            self.free = False

    def set_occupant(self,name):
      # if the seat is free, we need to assign an occupant  
        if self.free:
            self.occupant = name
            self.free = False
            
            print("The seat is now occupied by " + name)
            
        else:
            print("The seat is not free")
            

    def remove_occupant(self, name):
        if not self.free:
            old_name = self.occupant
            self.occupant = " "
            self.free = True

            print("The seat is free and was occupied by " + old_name)
    
s = Seat()                   # create an object
s.set_occupant("Sitara")
s.set_occupant("Neha")
s.remove_occupant("Sitara")


class Table:
       
    def __init__(self, capacity):
        self.capacity = capacity
        self.seats = [Seat(True, " ") for _ in range(capacity)]

    def has_free_spot(self):
        for seat in self.seats:
            if seat.free:
                
                return True
        return False

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






t = Table(6)
t.has_free_spot()
t.assign_seat("Sitara")
t.assign_seat("Neha")
t.left_capacity()            