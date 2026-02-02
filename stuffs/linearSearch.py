names = ["matt", "mark", "natalie", "billy", "bob", "bill", "jebadiah", "juan", "marc", "dominic"]
toFind = input("enter the data you wish to find: ")
found = False
while found != True:
    for i in range(0, len(names)):
        if names[i] == toFind:
            print("data found")
            found = True
    if found == False:
        print("data not in array")
    found = True
            