carSpaces = [
    ["empty", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty", "empty", "empty"]
]


#>--------------------------------<#

def emptyCarPark():
    for i in range(len(carSpaces)):
        for j in range(len(carSpaces[i])):
            carSpaces[i][j] = "empty"

def parkACar():
    regNum = input("enter the registration number: ") 
    column = int(input("enter the column your car is parked: ")) -1
    row = int(input("enter the row your car is parked: ")) -1
    while carSpaces[column][row] != "empty":
        print("car space is surrently occupied")
        column = int(input("re-enter the column your car is parked: ")) -1
        row = int(input("re-enter the row your car is parked: ")) -1
    
    carSpaces[column][row] = regNum
    print("Your car has been registered in the car park.")

def removeACar():
    findRegNum = input("enter the register number of your car: ")
    found = False
    for i in range(len(carSpaces)):
        for j in range(len(carSpaces[i])):
            if carSpaces[i][j] == findRegNum:
                carSpaces[i][j] = "empty"
                found = True
                print("car removed, thank you for trusting us with your car")
            else:
                found = False
    if found == False:
        tryAgain = input("sorry, your car is not in our system. you may try again or quit: ")
        if tryAgain == "try again":
            removeACar()
        elif tryAgain == "quit":
            print("returning...")
    elif found == True:
            print("car removed, thank you for trusting us with your car")


def DisplayGrid():
    emptySpaces = 0
    for i in range(len(carSpaces)):
        print(carSpaces[i])
    for i in range(len(carSpaces)):
        for j in range(len(carSpaces[i])):
            if carSpaces[i][j] == 'empty':
                emptySpaces += 1
    print("there are " + str(emptySpaces) + " left in the car park.")
    

#>--------------------------------<#

print("""
      1. Reset all spaces in the car park to "empty"
      2. Park a car
      3. Remove a car
      4. Display the car park grid
      5. Quit
""")
option = input("enter your choice: ")
while option != "5":
    match option:
        case "1":
            emptyCarPark()
        case "2":
            parkACar()
        case "3":
            removeACar()
        case "4":
            DisplayGrid()
        case default:
            option = input("Invalid choice, please re-enter: ")
    print("""
      1. Reset all spaces in the car park to "empty"
      2. Park a car
      3. Remove a car
      4. Display the car park grid
      5. Quit
    """)
    option = input("Enter your choice: ")
print("goodbye!")