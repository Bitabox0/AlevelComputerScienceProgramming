class Tree:

    def __init__(self, root):
        self.root = Node(None, root, None)

    def preOrder(self, p):
        print(p.getData())
        if p.getLeft() != None:
            self.preOrder(p.getLeft())
        if p.getRight() != None:
            self.preOrder(p.getRight())

    def inOrder(self, p):
        if p.getLeft() != None:
            self.inOrder(p.getLeft())
        print(p.getData())
        if p.getRight() != None:
            self.inOrder(p.getRight())

    def postOrder(self, p):
        if p.getLeft() != None:
            self.postOrder(p.getLeft())
        if p.getRight() != None:
            self.postOrder(p.getRight())
        print(p.getData())

    def addNode(self, n):
        if n 
        
    




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
    
    def setLeft(self, newLeft):
        self.left = newLeft

    def setRight(self, newRight):
        self.right = newRight
    
# tree = [
#     [1, "24", 3],
#     [5, "15", 2],
#     [-1, "17", -1],
#     [4, "38", 6],
#     [-1, "29", -1],
#     [-1, "9", -1],
#     [-1, "58", -1],
# ]
    

binaryTree = Tree(24)

# print(binaryTree.root)
binaryTree.inOrder(binaryTree.root)