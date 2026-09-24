myList = [12, 54, 1, 7, 53, 74, 34, 42, 13, 29, 3]

swapped = True

while swapped == True:
    swapped = False
    for i in range(0, len(myList)-1):
        if myList[i] > myList[i+1]:
            temp = myList[i]
            myList[i] = myList[i+1]
            myList[i+1] = temp
            swapped = True
    
print(myList)