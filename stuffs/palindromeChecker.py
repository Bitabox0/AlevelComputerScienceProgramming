letters = []

def push(data):
    letters.append(data)

def pop():
    return letters.pop()

def isempty():
    if len(letters) == 0:
        print("stackis empty")
    else:
        print("stack is not empty")

def checksize():
    print(len(letters))

# isempty()
# add("E")
# add("Y")
# print(letters)
# isempty()
# remove()
# add("T")
# checksize()
# print(letters)

word = input("enter world to check: ")
print(word)

for i in range(len(word)):
    push(word[i])

print(letters)

reverse = []

for i in range(len(letters)):
    reverse.append(pop())

print(reverse)

rev = "".join(reverse)
if rev == word:
    print("this is a palindrome")
else:
    print("this is not a palindrome")
