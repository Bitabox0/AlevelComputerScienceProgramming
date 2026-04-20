class Node():
    def __init__(self, theValue):
        self.value = theValue
        self.nextNode = None

    def getValue(self):
        return self.value
    
    def getNextNode(self):
        return self.nextNode
    
    def setValue(self, newValue):
        self.value = newValue

    def setNextNode(self, newNextNode):
        self.nextNode = newNextNode


node1 = Node("bob")
print(node1.getValue())
print(node1)
print(node1.getNextNode())

headpointer = node1


node2 = Node("tony")
node3 = Node("Matt")
node4 = Node("Gio")
node5 = Node("steve")

headpointer.setNextNode(node2)
headpointer.getNextNode().setNextNode(node3)
headpointer.getNextNode().getNextNode().setNextNode(node4)
headpointer.getNextNode().getNextNode().getNextNode().setNextNode(node5)

print("<------------------------------------->")

# print(node1.getValue())
# print(node2.getValue())
# print(node3.getValue())
# print(node4.getValue())
# print(node5.getValue())

print(headpointer.getValue())
print(headpointer.getNextNode().getValue())
print(headpointer.getNextNode().getNextNode().getValue())
print(headpointer.getNextNode().getNextNode().getNextNode().getValue())
print(headpointer.getNextNode().getNextNode().getNextNode().getNextNode().getValue())

print("<---------------------------------------------------->")

currentPointer = headpointer
while currentPointer != None:
    print(currentPointer.getValue())
    currentPointer = currentPointer.getNextNode()

print("<---------------------------------------------------->")

class LinkedList():
    def __init__(self, newHeadData):
        self.head = Node(newHeadData)

    