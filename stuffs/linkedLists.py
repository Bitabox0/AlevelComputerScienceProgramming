#>------ LINKED LIST CLASS ------<#

class LinkedList():
    def __init__(self, headData):
        self.head = Node(headData)

    def getHead(self):
        return self.head
    
    def add(self, newData):
        return None
    
    def traverseList(self):
        # check if empty
        # start at head
        # output item
        # got to next pointer
        # output item
        # repeat until end
        if self.head == None:
            print("the list is currently empty")
        else:
            while self.head != None:
                print(myList.getHead().getData())

#>------ NODE CLASS ------<#

class Node:
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data
    # def setData(self, newData):
    #     self.data = newData
    
    def getNext(self):
        return self.next
    def setNext(self, newNext):
        self.next = newNext

#>------ MAIN CODE ------<#

#instantiated linked list with first person
firstPerson = input("what us the first person in your list: ")
myList = LinkedList(firstPerson)

print(myList)
print(myList.getHead())

print(myList.getHead().getData())


