from sys import stdin
data = list(map(int, stdin.readline().rstrip()))
print(data) #디버깅

total = 0
for i in data:
    if(i == 0 or i == 1):
        total += i
    else:
        if(total == 0):
            total += 1
        total *= i

print(total)