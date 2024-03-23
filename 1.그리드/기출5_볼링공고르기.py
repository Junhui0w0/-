from sys import stdin
N, M = map(int, stdin.readline().split()) #N = 공 갯수 / M = 공의 최대 무게
ball_lst = list(map(int, stdin.readline().rstrip().split()))

way = 0
for i in range(0,N):
    for j in range(i,N):
        if(ball_lst[i] != ball_lst[j]):
            way += 1

print(way)