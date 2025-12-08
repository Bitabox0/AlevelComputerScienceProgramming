def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

x = fib(7)
print(x)

def fibonacci2(n):
    x=1