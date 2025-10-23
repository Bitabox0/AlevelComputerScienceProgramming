#Develop a Python class for a Student. 
#The constructor should take parameters for the student's name, ID, and university major. 
#Implement private attributes for these parameters. (Cant do cos Python)
#Create methods to get and set the student's major, as well as to display the student's information. 

#Instantiate more than one object from the class, and show suitable testing.

class student: #creates a class for student
    
    def __init__(self, studentName, studentID, studentMajor): #creates a constructor method for student
        self.name = studentName #creates an attribute for the student's name
        self.ID = studentID #creates an attribute for the student's ID
        self.major = studentMajor #creates an attribut for the student's major

inputedName = input("please enter name of student: ") #asks the user to input the student's name 
inputedID = input("please enter student's ID: ") #asks the user to input the student's ID
inputedMajor = input("please enter student's major: ") #asks the user to input the student's major

student1 = student(inputedName, inputedID, inputedMajor) #instantiates three objects in the class "student"
print("student's name: " + student1.name) #prints the user's set attribute of the student's name
print("student's ID: " + student1.ID) #prints the user's set attribute of the student's ID
print("student's major: " + student1.major) #prints the user's set attribute of the student's major