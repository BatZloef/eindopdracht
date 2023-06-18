from slot import Slots

class Stations:
    def __init__(self,naam,id,locatie,capacity):
        self.naam = naam
        self.id = id
        self.locatie = locatie
        self.capacity = capacity
        self.slots = [Slots() for i in range(capacity)]
        self.bikes = []
        self.open_slots = []
    def add_bike(self, bike):
        if self.open_slots > 0:
            self.bikes.append(bike)
            self.open_slots -= 1
        else:
            print("Geen plaats meer in station")
    def remove_bike(self, bike):
        if bike in self.bikes:
            self.bikes.remove(bike)
            self.open_slots += 1
        else:
            print("Fiets niet gevonden in station")