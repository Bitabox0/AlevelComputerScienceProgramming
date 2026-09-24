tree1 = [
    [1, "M", 2],
    [3, "H", 4],
    [5, "T", 6],
    [-1, "D", -1],
    [-1, "K", -1],
    [-1, "R", -1],
    [-1, "X", -1],
]

tree2 = [
    {
        "Left": 1, 
        "Data": "M", 
        "Right": 2
    },
    {
        "Left": 3, 
        "Data": "H", 
        "Right": 4
    },
    {
        "Left": 5, 
        "Data": "T", 
        "Right": 6
    },
    {
        "Left": -1, 
        "Data": "D", 
        "Right": -1
    },
    {
        "Left": -1, 
        "Data": "K", 
        "Right": -1
    },
    {
        "Left": -1, 
        "Data": "R", 
        "Right": -1
    },
    {
        "Left": -1, 
        "Data": "X", 
        "Right": -1
    },
    ]

tree = [
    [1, "F", 5],
    [2, "D", -1],
    [3, "B", 4],
    [-1, "A", -1],
    [-1, "C", -1],
    [6, "H", 7],
    [-1, "G", -1],
    [-1, "J", 8],
    [-1, "Z", -1],
]

print("pre order")

def preOrder(p):
    print(tree[p][1])
    if tree[p][0] != -1:
        preOrder(tree[p][0])
    if tree[p][2] != -1:
        preOrder(tree[p][2])
preOrder(0)

print("###########################################")
print("in order")

def inOrder(p):
    if tree[p][0] != -1:
        inOrder(tree[p][0])
    print(tree[p][1])
    if tree[p][2] != -1:
        inOrder(tree[p][2])
inOrder(0)
        
print("###########################################")
print("post order")

def postOrder(p):
    if tree[p][0] != -1:
        postOrder(tree[p][0])
    if tree[p][2] != -1:
        postOrder(tree[p][2])
    print(tree[p][1])
postOrder(0)
