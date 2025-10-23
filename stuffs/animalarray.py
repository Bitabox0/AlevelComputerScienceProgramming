animal = ["dog", "cat", "lizard"]

for i in range(len(animal)):
    print(animal[i])

found = False
check = "dog"
for i in range(len(animal)):
    if animal[i] == check:
        found = True
        print("found")

