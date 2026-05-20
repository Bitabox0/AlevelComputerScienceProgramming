q = []
maxSize = 10
size = 0

def enqueue(item, q):
    global size
    q.append(item)
    size = size + 1

def dequeue(item, q):
    ret = print(q[0])
    q.remove()
    size = size - 1
