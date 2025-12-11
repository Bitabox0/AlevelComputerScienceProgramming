class Animals:
    
    def __init__(self, speciesA, nameA):
        self.species = speciesA
        self.name = nameA
    
    def info(self):
        print("animal name: " + self.name)
        print("animal species: " + self.species)

class Gorilla(Animals):

    def __init__(self, mateG, speciesA, nameA):
        self.mate = mateG
        super().__init__(speciesA, nameA)


    def health(self):
        print(self.name + " is a " + self.species + " and is in healthy condition.")
        print(self.name + "'s mate is " + self.mate)

gorilla1 = Gorilla("mini", "gorilla gorilla", "inana")
gorilla1.info()
gorilla1.health()
