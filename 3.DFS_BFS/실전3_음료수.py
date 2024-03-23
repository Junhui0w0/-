from sys import stdin
N , M = map(int, stdin.readline().rstrip().split())

my_map = list()
for _ in range(N): #0이 뭉쳐져있음. . . total += 1
    my_map.append(list(map(int, stdin.readline().rstrip())))
print(my_map) #디버깅

def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= M: #만약 x,y가 맵 밖으로 나가면
        return False
    if(my_map[x][y] == 0):
        my_map[x][y] = 1  
        dfs(x-1,y) 
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

total = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            total += 1

print(total)