items = ["", "", "", "", ""]

top = 0

def push(data):
    global top
    items[top] = data
    top =+ 1
    return top

def pop():
    global top
    items[top] = ""
    top =- 1
    return top

def isfull():
    if top == 5:
        print("this stack is full")

def isEmpty():
    if top == 0:
        print("this stack is empty")

isEmpty()
push("data")
push("data")
push("data")
pop()
push("data")
push("data")
isfull()