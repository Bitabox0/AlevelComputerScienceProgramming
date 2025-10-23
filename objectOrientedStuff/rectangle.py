#Define a Python class for a Rectangle.
#The constructor should take parameters for the length and width of the rectangle.
#Implement private attributes for these parameters.
#Create methods to calculate the area and perimeter of the rectangle.

#Instantiate more than one object from the class, and show suitable testing.  

class rectangle: #creates a class for rectangle
    
    def __init__(self, rWidth, rLength): #creates constructor method for rectangle
        self.width = rWidth #creates attribute for rectangles width
        self.length = rLength #creates attribute for rectangle length

    def area(self): #creates a function inside the class that calculates the area
        return self.width * self.length

    def perimeter(self): #creates a function inside the class that calculates the perimeter
        return (2*self.width) + (2*self.length)

inputedwidth = int(input("please enter width of rectangle: ")) #asks the user to input rectangle width
inputedlength = int(input("please enter length of rectangle: ")) #asks the user to imput rectangle length

rectangle1 = rectangle(inputedwidth, inputedlength) #intsantiates two objects in the class "rectangle"
print(rectangle1.area()) #prints the area function using inputed width and length
print(rectangle1.perimeter()) #prints the perimeter function using inputed width and length