from sys import stdin
from collections import deque
N,M = map(int,stdin.readline().rstrip().split()) #NxN 배열 list 0=빈공간 / 1=집 / 2=치킨

my_map = deque()
house_index = deque() #1
chicken_index = deque() #2

c = 1 #열
for i in range(1,N+1):
    put_data = list(map(int, stdin.readline().rstrip().split()))
    my_map.append(put_data)
    for j in put_data:
        if(j == 1):
            house_index.append((i,c))
        elif(j == 2):
            chicken_index.append((i,c))
        c += 1
    c = 1

print(my_map)
print(house_index)
print(chicken_index)
    
distance = deque()
total = 0
for j in range(len(chicken_index)):
    for i in range(len(house_index)):
        total += abs(house_index[i][0] - chicken_index[j][0]) + abs(house_index[i][1] - chicken_index[j][1])
    distance.append(total)
    total =0

print(distance)