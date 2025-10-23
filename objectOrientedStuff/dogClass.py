#Create a Class for a dog in python. Implement private attributes using the _attribute approach in python. 
# When a dog is instantiated the constructor takes in two parameters, the name and colour. These are the only attributes within the dog class. 
# Also create a method that will take in a parameter integer and then output "Woof!" the number of times the value of the parameter. 
# Create the necessary getter and setter methods for the object. Instantiate a new instance of a dog. 
# output its name and colour in a single message e.g. Hello Fido, you are a Brown colour. 
# Make the dog woof 10 times. 
# output the memory location of the Dog object you have instantiated. 

class Dog: #creates a class for dog
    def __init__(self, dogName, dogColour):
        self.name = dogName #creates an attribute for the name of the dog
        self.colour = dogColour #creates an attribute for the colour of the dog

#>---------------------------------------------------------------------------------<#

def wooftimes(numberOfWoofs): #creates a procedure for a loop
    for i in range(numberOfWoofs):
        print("woof!")

doggyName = input("enter the name of the dog: ") #asks the user to input the name of the dog
doggyColour = input("enter the colour of the dog: ") #asks the user to input the colour of the dog


numberOfWoofs = 10 #gives a value for the number of times the loop should run for 
dog1 = Dog(doggyName, doggyColour) #instanistises an object to the class so that it can be called later


print("hello " + dog1.name + "! you are " + dog1.colour + "!") #concatinateds the users input into a sentence
wooftimes(numberOfWoofs) #calls the procedure to run
print(dog1) #prints the location of the the data in memory
