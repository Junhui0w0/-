from sys import stdin
N = int(stdin.readline()) #0시 ~ N시 59분 59초

total = 0
for i in range(0,N+1):
    for j in range(0,60):
        for k in range(0,60):
            lst = list(str(i) + str(j) + str(k))
            if('3' in lst):
                total += 1

print(total)