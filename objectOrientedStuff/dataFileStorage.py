# create a class for person working at company
# have it define name, salary or hours, id, and access level
# then store the data in a 2d array
# then save that data to a file using file handling

    #>-------------------------------------------------------------------------------<#

data = []

class Worker:

    def __init__(self, Wname, Wsalary, Whours, Wid, WaccessLevel, WpayType):
        self.name = Wname
        self.salary = Wsalary
        self.hours = Whours
        self.id = Wid
        self.accessLevel = WaccessLevel
        self.payType = WpayType

    #>-------------------------------------------------------------------------------<#

    def salaryOrHours(self):
        SalaryOrHours = input("is " + self.name + " salary or hours? [S/H]: ")
        if SalaryOrHours == "S":
            self.payType = "Salary"
        elif SalaryOrHours == "H":
            self.payType = "Hours"
        else:
            print("please enter S or H")

    #>-------------------------------------------------------------------------------<#

    def toList(self):
        if self.payType == "S":
            return [self.name, self.salary, self.id, self.accessLevel]
        elif self.payType == "H":
            return [self.name, self.hours, self.id, self.accessLevel]
        
    #>-------------------------------------------------------------------------------<#

while True:        
    inputedName = input("please enter the worker's name: ")
    inputedSalary = input("please enter the worker's salary (if any): ")
    inputedHours = input("please enter the worker's hours (if any): ")
    inputedID = input("please enter the worker's ID: ")
    inputedAccessLevel = input("please enter the worker's access level: ")
    inputedPayType = input("please enter the worker's pay type: ")

    newWorker = Worker(inputedName, inputedSalary, inputedHours, inputedID, inputedAccessLevel, inputedPayType)
    data.append(newWorker.toList())

    another = input("Add another worker? [Y/N]: ").strip().upper()
    if another != "Y":
        break

    #>-------------------------------------------------------------------------------<#

file = open("workers.txt", "w")
for worker in data:
    file.write(",".join(str(item) for item in worker) + "\n")
print("\nAll workers saved successfully!")

