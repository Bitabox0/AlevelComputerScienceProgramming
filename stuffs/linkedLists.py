#>------ LINKED LIST CLASS ------<#

class LinkedList():
    def __init__(self, headData):
        self.head = Node(headData)

    def getHead(self):
        return self.head
    
    def add(self, newData):
        return None
    
#>------ NODE CLASS ------<#

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getName(self):
        return self.data
    def setName(self, newData):
        self.data = newData
    
    def getNext(self):
        return self.next
    def setNext(self, newNext):
        self.next = newNext

#>------ MAIN CODE ------<#

firstPerson = input("what us the first person in your list: ")
myList = LinkedList(firstPerson)

print(myList)
print(myList.getHead())

print(myList.getHead().getData())

person1 = Node("bob")
person2 = Node("john")
person3 = Node("matt")
person4 = person2

print(person1)
print(person2)
print(person3)

print(person1.getName())
print(person2.getName())
print(person3.getName())

print(person4.getName())
print
