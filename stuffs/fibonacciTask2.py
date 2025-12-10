import time as t

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)



def fibonacci2(n):
    fibNumbers = [0, 1]

    for i in range(2, n+1):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
    
    return fibNumbers[n]

start1 = t.time()
fib(30)
stop1 = t.time()
totalTime1 = stop1 - start1
formatTime1 = "{:.10f}".format(totalTime1)
print("recursive", formatTime1)

start2 = t.time()
fibonacci2(30)
stop2 = t.time()
totalTime2 = stop2 - start2
formatTime2 = "{:.10f}".format(totalTime2)
print("iterative", formatTime2)
