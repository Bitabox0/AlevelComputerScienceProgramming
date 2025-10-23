import time

def main_menu():

    print("""
    1: Play game
    2: Scoreboard
    3: Settings
    4: End game
    """)

    choice = int(input("enter choice: "))

    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        choice = int(input("not and option. enter what you would like to do:"))

    match choice:
        case 1:
            playing_game()
        case 2:
            print("you aint first icl...")
        case 3:
            print("settings open")
        case 4:
            print("Quitting game...")
            time.sleep(3)
            print("Game ended... Why?")
    

def playing_game():
    print("yea ur playing the game mate")
    time.sleep(10)
    main_menu()



main_menu()
