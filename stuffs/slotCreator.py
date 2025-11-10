slots = [
    [],
    [],
    [],
    [],
    [],
]

def addSlots(): #defines (?) a prodecure
    for i in range(len(slots)): #prints each inner array in the 2d array "slots"
        print(slots[i])
    slotChoice = input("enter the slot you wish to use: ") #asks the user for an input
    slotName = input("enter the name of your character: ") #asks the user for an input
    slotDifficulty = input("enter the difficulty of the slot(easy, normal, hard, nightmare): ") #asks the user for an input

    match slotChoice: #matches the input of "slotChoice" to certain inputs
        case "1":
            slots[0].append(slotName) #adds the inputs to the first slot
            slots[0].append(slotDifficulty)
        case "2":
            slots[1].append(slotName) #adds the inputs to the second slot
            slots[1].append(slotDifficulty)
        case "3":
            slots[2].append(slotName) #adds the inputs to the third slot
            slots[2].append(slotDifficulty)
        case "4":
            slots[3].append(slotName) #adds the inputs to the fourth slot
            slots[3].append(slotDifficulty)
        case "5":
            slots[4].append(slotName) #adds the inputs to the fifth slot
            slots[4].append(slotDifficulty)
        case "exit":
            gameMenu()
    for i in range(len(slots)): #prints each inner array in the appended 2d array "slots"
        print(slots[i])

def gameMenu():
    gameChoice = 0
    while gameChoice != 4: #will continue to execute the code in the array until a condition is met
        print("""
    1: Play game
    2: Character select
    3: Settings
    4: Quit
        """)
        gameChoice = int(input("enter what you would like to do: ")) #asks the user for an input
        match gameChoice: #matches the input of "gameChoice" to certain choices
            case 1:
                print("playing game...")
            case 2:
                addSlots()
            case 3:
                print("in settings...")
            case 4:
                print("quitting...")
gameMenu()