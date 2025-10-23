#Design a Python class for a Bank Account.
#The constructor should take parameters for the account holder's name and initial balance. 
#Implement private attributes for these parameters. 
#Create methods to deposit and withdraw money from the account, as well as to display the account's balance.

#Instantiate more than one object from the class, and show suitable testing. 

class bankAccount:

    def __init__(self, userName, initialBalance):
        self.name = userName
        self.balance = initialBalance

    def deposit(self, depMoney):
        self.balance = self.balance + int(depMoney)
        print("leaving...")

    def withdraw(self, witMoney):
        
        if self.balance > 0:
            self.balance = self.balance - int(witMoney)
        elif self.balance <= 0:
            print("""not enough money.
                going to deposit...""")
            depMoney = input("please enter the money you would like to deposit: ")
            print(self.deposit(depMoney))
        print("leaving...")
    
    def showBalance(self):
        return self.balance



def startingStuff(name1, initialBalance1):
    
    action = False
    witORdep = input("withdraw(1) or deposit(2) or show money(3) or exit(4)")
    if witORdep == "2":
        depMoney = input("please enter the money you would like to deposit: ")
        print(account1.deposit(depMoney))
    elif witORdep == "1":
        witMoney = input("how much money would you like to withdraw: ")
        print(account1.withdraw(witMoney))
    elif witORdep == "3":
        print(account1.name + "'s balance = £" + str(account1.showBalance()))
    elif witORdep == "4":
        print("leaving...")
        action = True
    else:
        print("not an option, choose 1, 2, 3 or 4")
    return action

name1 = input("enter the name for your account: ")
initialBalance1 = int(input("enter the initial balance of your account: "))
account1 = bankAccount(name1, initialBalance1)
action = False
while action == False:
    action = startingStuff(name1, initialBalance1)