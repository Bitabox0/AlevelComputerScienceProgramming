class Animal:
    def __init__(self, name):
      
      	# Storing the name of the animal
        self.name = name  

    def sound(self):
      
        # This method should be implemented by subclasses
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def sound(self):
      
        # Dog-specific sound
        return "Woof!"

# Creating instances
# Animal instance with generic name
a = Animal("Generic Animal")  

# Dog instance with name 'Buddy'
d = Dog("Buddy")  

# Accessing attributes and methods
print(a.name)  # Output: Generic Animal
print(d.name)    # Output: Buddy
print(d.sound())  # Output: Woof!