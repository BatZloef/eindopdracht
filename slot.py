class Slots: 
    def __init__(self):
        self.fiets = None
    
    def voeg_fiets(self, fiets):
        self.fiets = fiets
    
    def is_leeg(self):
        self.fiets = None