from user import *
from bike import *
from station import *
from slot import *
from log import *
from transporteur import *
from website import *


class System():
    def __init__(self):
        self.users = Gebruiker()
        self.bikes = Fiets()
        self.stations = Stations()
        self.slots = Slots()
        self.log = Log()
        self.transporters = Fietstransporteur()
        self.web = web()
    def terminal(self):
        keuze = "1: Fiets lenen\n2: Fiets terugzetten\n3: HTML bekijken\n4: Simulatie\n5: Stoppen"
        antwoord = int(input(keuze))
        while antwoord != 5:
            if antwoord == 1:
                print(self.users)
            elif antwoord == 2:
                print("2")
            elif antwoord == 3:
                print("3")
            elif antwoord == 4:
                print("4")
            else:
                print("Ongeldige invoer")
            antwoord = int(input(keuze))
