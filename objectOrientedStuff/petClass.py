import time as t
import random as r

class Pet:
    def __init__(self, Pname, Phappiness, Phunger):
        self.name = Pname
        self.happiness = Phappiness
        self.hunger = Phunger
    
    def hungry(self):
        print("IO am here")

        while self.hunger >= 0:
            print("here now")
            t.sleep(1)
            self.hunger = self.hunger - 5
            print(self.hunger)
        if self.hunger < 0:
            self.hunger = 0
            print(self.name + " is out of hunger! Feed them quickly!!!")
        elif self.hunger <= 30:
            print(self.name + " only has " + str(self.hunger) + " hunger points left!")
        else:
            print(self.name + " has " + str(self.hunger) + " hunger points.")
    
    # active = False
    def happyLevel(self):
        print("IO am here")
        while self.happiness >= 0:
            print("IN THE WHILE")
            t.sleep(10)
            self.happiness = self.happiness - 5
            if self.happiness == 100:
                print(self.name + " is feeling fantastic!")
                return self.happiness
            elif self.happiness < 80:
                print(self.name + " is feeling good.")
                return self.happiness
            elif self.happiness < 50:
                print(self.name + " is feeling okay.")
                return self.happiness
            elif self.happiness < 25:
                print(self.name + " is feeling sad")
                return self.happiness
            elif self.happiness <= 0:
                self.happiness = 0
                print(self.name + " is feeling distraught! play with them or feed them some food!")
                return self.happiness
    
    # active = True
    def play(self):
        toy = input("enter the toy youre using: ")
        happyScore = r.randint(10, 30)
        print(toy + " gave " + str(happyScore) + " happiness points!")
        self.happiness = self.happiness + happyScore
        return self.happiness
    
    def feed(self):
        food = input("enter the toy youre using: ")
        foodScore = r.randint(10, 30)
        happyScore = r.randint(5, 15)
        print(food + " gave " + str(foodScore) + " hunger points and gave " + str(happyScore) + " happiness points!")
        self.hunger = self.hunger + foodScore
        self.happiness = self.happiness + happyScore
        return self.hunger and self.happiness
    
    # def huTick(self):
    # while self.hunger >= 0:
    # t.sleep(10)
    # self.hunger = self.hunger - 5
    # return self.hunger
    # def haTick(self):
    # while self.happiness >= 0:
    # self.happiness = self.happiness - 5
    # return self.happiness

quit = ""
inputedName = input("please enter your pet's name: ")
print(inputedName)
initialHunger = 100
initialhappiness = 100
pet1 = Pet(inputedName, initialHunger, initialhappiness)
pet1.hungry()
# print(pet1.huTick())
# print(pet1.haTick())
# print(pet1.hungry())
# print(pet1.happyLevel())
# quit = input("Would you like to quit? Type [Quit] to quit: ")