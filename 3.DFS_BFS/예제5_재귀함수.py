from sys import stdin

def factorial(i):
    global total
    total += i
    i += 1

    if(i == 10):
        return total

    return factorial(i)

n = int(stdin.readline().rstrip())
total = 0
print(factorial(n))