def multiples(table, startnum,  endnum, pupilName):
    print("hi " + pupilName +  "... here is your times tables")
    for i in range(startnum, endnum+1):
        print(str(table) + " x " + str(i) + " = " + str(table * i))

# answer = multiples(5, 4, 12, "bob")

start = input("would you like to start? Y/N: ")
if start == "Y":
    table = int(input("which multiplication table do you want to see: "))
    startnum = int(input("enter the number you wish the table to start at: "))
    endnum = int(input("enter the number you wish the table to end at: "))
    pupilName = input("please enter your name pupil: ")
    multiples(table, startnum,  endnum, pupilName)
elif start == "N":
    print("be like that then... ")