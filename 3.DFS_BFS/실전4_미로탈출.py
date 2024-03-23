from sys import stdin
N , M = map(int, stdin.readline().split())

my_map = list()
for _ in range(N):
    my_map.append(list(map(int, stdin.readline().rstrip())))
    
dx = [-1,1,0,0]
dy = [0,0,1,-1]

from collections import deque
def func(x,y): #시작 좌표 입력
    d = deque()
    d.append((x,y))
    
    while(len(d) != 0): #deque D가 빌 때 까지 반복
        x,y = d.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if(nx <= -1 or nx >= N or ny <= -1 or ny >= M): #움직인 좌표가 맵 밖으로 나간 경우
                continue
            if(my_map[nx][ny] == 0): #움직인 좌표가 벽인 경우
                continue
            if(my_map[nx][ny] == 1): #움직인 좌표가 길인 경우
                my_map[nx][ny] = 1 + my_map[x][y]
                d.append((nx,ny))
    return my_map[N-1][M-1]

print(func(0,0))