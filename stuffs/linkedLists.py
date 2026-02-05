#>------ LINKED LIST CLASS ------<#

class LinkedList():
    def __init__(self, headData):
        self.head = Node(headData)

    def getHead(self):
        return self.head
    
    def add(self, data):
        newNode = Node(data)
        current = self.head
        if self.head == None:
            self.head = newNode
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(newNode)
    
    def traverseList(self):
        current = self.head
        if current == None:
            print("the list is currently empty")
        else:
            print(current.getData())
            while current.getNext() != None:
                current = current.getNext()
                print(current.getData())

    def remove(self, data):
        current = self.head
        if current.getData() == data:
            current = current.getNext()
        else:
            while current.getNext().getData() != data:
                current = current.getNext()
            

                

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

myList.add("bob")
myList.add("amy")
myList.add("matt")
myList.add("Quayon")

print(myList.traverseList())