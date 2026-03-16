numbers = [None, None, None, None, None, None]
for i in range(0, len(numbers)):
    addToList = int(input("enter number: "))
    numbers[i] = addToList
total = 0
for i in range(len(numbers), 0, -1):
    print(numbers[i-1])
    total = total + numbers[i-1]
print(total / len(numbers))