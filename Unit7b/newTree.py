tree = [
    [1, "24", 3],
    [5, "15", 2],
    [-1, "17", -1],
    [4, "38", 6],
    [-1, "29", -1],
    [-1, "9", -1],
    [-1, "58", -1],
]

def preOrder(p):
    print(tree[p][1])
    if tree[p][0] != -1:
        preOrder(tree[p][0])
    if tree[p][2] != -1:
        preOrder(tree[p][2])
preOrder(0)

print("-----------------------------------------------")


def inOrder(p):
    if tree[p][0] != -1:
        inOrder(tree[p][0])
    print(tree[p][1])
    if tree[p][2] != -1:
        inOrder(tree[p][2])
inOrder(0)

print("-----------------------------------------------")

def postOrder(p):
    if tree[p][0] != -1:
        postOrder(tree[p][0])
    if tree[p][2] != -1:
        postOrder(tree[p][2])
    print(tree[p][1])
postOrder(0)


