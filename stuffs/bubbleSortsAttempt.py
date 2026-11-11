myList = [5, 3, 67, 23, 57, 68, 70, 28]

def bubbleSort():
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

def insertionSortWRONG():
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(1, len(myList)):
            if myList[i] < myList[i-1]:
                temp = myList[i-1]
                myList[i-1] = myList[i]
                myList[i] = temp
                swapped = True
    print(myList)

def trueInsertion():
    for i in range(1, len(myList)):
        temp = myList[i]
        position = temp - 1
        while position >= 0 and myList[position] > temp:
            myList[position+1] = myList[position]
            position = position- 1
        myList[position + 1] = temp

    print(myList)

trueInsertion()
