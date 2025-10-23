#Implement a Python class for a Shape. 
#This class should have methods to calculate the area and perimeter of the shape. 
#Then, create subclasses for specific shapes like Rectangle, Circle, and Triangle. 
#Each subclass should override the methods to calculate the area and perimeter based on its specific formula.
PI = 3.14
class Shapes:

    def __init__(self, sLength, sWidth):
        self.length = sLength
        self.width = sWidth

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (2*self.length) + (2*self.width)


class Rectangle(Shapes):

    # constructor to take on shapes attributes

    def area(self):
        pass
    
    def perimeter(self):
        pass
    
class Sphere(Shapes):
    def __init__(self, sRadius):
        self.radius = sRadius
    
inputedLength = 20
inputedWidth = 10

rectangle1 = Rectangle(inputedLength, inputedWidth)
print(rectangle1.area())
print(rectangle1.perimeter())

# https://www.ragie.ai/ (rag ai)
# https://www.w3schools.com/python/python_inheritance.asp
# https://www.google.com/search?q=inherit+attributes+from+parent+class+python&oq=inherit+attributes&gs_lcrp=EgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyBggBEEUYOTIICAIQABgWGB4yCAgDEAAYFhgeMggIBBAAGBYYHjIICAUQABgWGB4yCAgGEAAYFhgeMggIBxAAGBYYHjIICAgQABgWGB4yCAgJEAAYFhge0gEINTYwN2owajGoAgCwAgA&sourceid=chrome&ie=UTF-8&surl=1&safe=active&ssui=on
# https://docs.google.com/document/d/18zjvVAgXgyL51ioj9yeorX10iZNUGc245yUN0jsRhKg/edit?tab=t.0