#Create a Python class for a Bank. 
#Implement a constructor that initializes an empty list to store bank accounts. 
#Create methods to add a new account to the bank, find an account by account number, deposit money into an account, withdraw money from an account, and display all accounts' information. 
#Instantiate more than one object from the class, and show suitable testing.  

class Bank: #creates a class for bank

    def __init__(self, accName, accBalance, accNum): #creates a constructor method for bank
        self.name = accName  #create attribute for account name
        self.balance = accBalance #create attribute for the account balance
        self.num = accNum #create attribute for the account number

    def deposit(self, depAmount): #creates a method to deposit money
        self.balance = self.balance + depAmount #calculates money deposited
        return self.balance #returns value
    
    def withdraw(self, witAmount): #creates a method to withdraw money
        self.balance = self.balance - witAmount #calculates money withdrew
        return self.balance #return value
    
    def accountDetails(self): #creates a method to display account details
        print("showing account details for " + account1.name) #prints account name
        print("account number: " + account1.num) #prints account number
        print("balance £" + str(account1.balance)) #prints account balance

userName = "Ivan123" #assigns the account name to the variable
userBalance = 1000 #assigns the account balance to the variable
userNum = "1353636363" #assigns the account number to the variable

account1 = Bank(userName, userBalance, userNum) #instantiates(creating) three objects in the class "Bank"
depAmount = 200 #assigns how much is being deposited
witAmount = 500 #assigns how much is being withdrew
print(account1.deposit(depAmount)) #prints deposit method
print(account1.withdraw(witAmount)) #prints withdraw method
print(account1.accountDetails()) #prints account details method