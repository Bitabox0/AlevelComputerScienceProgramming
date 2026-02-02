class Node:
    def __init__(self, data):
        self.data = data
        self.next = "null"

    def getName(self):
        return self.data
    def setName(self, newData):
        self.data = newData
    
    def getNext(self):
        return self.next
    def setNext(self, newNext):
        self.next = newNext


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

