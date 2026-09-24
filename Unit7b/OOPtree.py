class Tree:

    def __init__(self, root):
        self.root = root

class Node:

    def __init__(self, left, data, right):
        self.left = left
        self.data = data
        self.right = right

    def getLeft(self):
        return self.left
    
    def getData(self):
        return self.data

    def getRight(self):
        return self.right
    


node2 = Node(None, "17", None)
node4 = Node(None, "29", None)
node5 = Node(None, "9", None)
node6 = Node(None, "58", None)
node1 = Node(node5, "15", node2)
node3 = Node(node4, "38", node6)
node0 = Node(node1, "24", node3)



root = Tree(node1)

def preOrder(p):
    print(p.getData())
    if p.getLeft() != None:
        preOrder(p.getLeft())
    if p.getRight() != None:
        preOrder(p.getRight())
preOrder(node0)

print("-----------------------------------------------")

def inOrder(p):
    if p.getLeft() != None:
        inOrder(p.getLeft())
    print(p.getData())
    if p.getRight() != None:
        inOrder(p.getRight())
inOrder(node0)

print("-----------------------------------------------")

def postOrder(p):
    if p.getLeft() != None:
        postOrder(p.getLeft())
    if p.getRight() != None:
        postOrder(p.getRight())
    print(p.getData())
postOrder(node0)

print("-----------------------------------------------")

