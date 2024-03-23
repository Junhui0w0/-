import math
import time
start = time.time()

from sys import stdin
N = int(stdin.readline())
x,y= 1,1
direction = list(map(str, stdin.readline().rstrip().split()))

for i in range(N):
    if(direction[i] == 'R'):
        if(y + 1 != 6):
            y += 1
    elif(direction[i] == 'U'):
        if(x - 1 != 0):
            x -= 1
    elif(direction[i] == 'D'):
        if(x + 1 != 6):
            x += 1
    elif(direction[i] == 'L'):
        if(y - 1 != 0):
            y -= 1
print(x,y)

end = time.time()

print(f"{end - start:.5f} sec")