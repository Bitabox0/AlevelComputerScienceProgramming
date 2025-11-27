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
            carSpaces[i][j] = "i"
        print(carSpaces[i])

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
#         #case "2":
#             #parkACar()
#         #case "3":
#             #removeACar()
#         #case "4":
#             #DisplayGrid()
#         case default:
#             option = input("Invalid choice, please re-enter: ")
    print("""
      1. Reset all spaces in the car park to "empty"
      2. Park a car
      3. Remove a car
      4. Display the car park grid
      5. Quit
    """)
    option = input("Enter your choice: ")
print("goodbye!")