import random

class Gebruiker:
    def __init__(self, naam):
        self.lijst = []
        self.fiets = None
        self.index = 1

    def toevoegen(self, voornaam, achternaam):
        voornaam = ["Nico","Nick","Yana","Amber","Kenji","Kay","Yarno","Robbe","Jelle","Daan","Noah","Tjade"]
        achternaam = ["Meeusen","Vanreusel","Langenakers","Caluij","Omblets","Goris","Voet","Vanlooveren","Leclerq","Vermeulen","Wezenbeek","Lauwers"]
        naam = random.choice(voornaam) + " " + random.choice(achternaam)
        nieuwe_gebruiker = Gebruiker(self.index, naam)
        self.lijst.append(nieuwe_gebruiker)
        self.index += 1
    def __str__(self):
        tekst = "\nHier is een lijst van de gebruikers:\n"
        for gebruiker in self.lijst:
            tekst += str(gebruiker) + "\n"
        return tekst