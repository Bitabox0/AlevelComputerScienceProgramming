import time
def createaccount():
    valid = False
    username = input("enter a username for your account: ")#what the user inputs
    while valid != True:#loops until the valid condition is met
        password = input("enter a password for your account: ")#what the user inputs
        if password == username:#checks if the password and username are the same
            print("password cant be the same as username")
        else:
            if len(password) < 8:# checks if the password is loinger than 8 characters
                print("password must be atleast 8 characters long")
            else:
                if not password.isdigit() and password.isalpha():#checks if the password contains letters and numbers
                    print("password must contain both letters and numbers")
                else:
                    print("password is valid, welcome!")
                    balance = 0
                    valid = True
                   
    return username, password, balance
    createorlog()

def login(username, password, balance):
    count = 0
    loggedin = False
    while loggedin == False:
        loguser = input("please enter your username: ")
        logpass = input("please enter your password: ")
        if loguser == username and logpass == password:
            print("Welcome!")
            loggedin = True
            actions(balance)
        else:
            print("username or password is incorrect. Please try again")
            count = count + 1
            if count >= 3:
                print("Too many attempts failed. Please try again in 10 seconds...")
                time.sleep(10)
                loggedin = False
       
def createorlog():
    username = ""
    password = ""
    while True:
        createorlog = input("would you like to create an account, log into your account or quit: ")
        if createorlog == "create":
                username, password, balance = createaccount()
        elif createorlog == "login":
            if username == "" and password == "":
                print("no account found. Please try again.")
            else:
                login(username, password, balance)
        elif createorlog == "quit":
            print("goodbye!")
            break
        else:
            print("invalid response. Please choose 'create', 'login' or 'quit'.")

def withdraw(balance):
    while True:
        if balance <= 0:
            print("you currently have no money to withdraw.")
            Wdep = input("would you like to deposit money? ")
            if Wdep == "yes":
                balance = deposit(balance)
                break
            else:
                print("Going back...")
                break
        else:
            withdraw = int(input("you currently have £" + str(balance) + ". how much would you like to withdraw: "))
            if withdraw <= balance:
                balance = balance - withdraw
                print("you now have £" + str(balance) + ".")
                break
            elif withdraw > balance:
                print("Sorry, you do not have enough money to withdraw this amount.")
                Wgoback = input("would you like to try again or go back")
                if Wgoback == "back":
                    break

    return balance

def deposit(balance):
    deposit = int(input("how much would you like to deposit: "))
    balance = balance + deposit
    print("£" + str(deposit), "has been deposited to your account. Going back...")
    return balance
   


def actions(balance):
    while True:
        action = input("Would you like to withdraw, check, or deposit your balance! or would you like to quit: ")
        if action == "check":
            print("your balance is £" + str(balance) + ".")
        elif action == "withdraw":
            balance = withdraw(balance)
        elif action == "deposit":
            balance = deposit(balance)
        elif action == "quit":
            print("Going Back...")
            break
        else:
            print("invalid response. Please choose 'check', 'withdraw', 'deposit' or 'quit'.")
            break


createorlog()