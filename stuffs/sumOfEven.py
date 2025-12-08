def sumOfEven(n):
    total = 0
    if n <= 0:
        print(n)
    else:
        print(n)
        total = n + sumOfEven(n - 2)
    return total

x = sumOfEven(4)
print(x)
