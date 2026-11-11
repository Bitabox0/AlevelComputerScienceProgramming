# import random
# y = random.randint(1,6)
# print(y)


import random
number = random.randint(1, 100)
count = 7
guess = int(input("guess a number between 1 and 100, you have 7 guesses: "))
while guess != number and count >= 0 :
  if guess > number:
    print("too high")
  elif guess < number:
    print("too low")
  count = count - 1
  guess = int(input("try again, you only have " + str(count) + " guesses left: "))

if count <= 0:
  print("out of lives!")
elif guess == number:
  print("you won!")