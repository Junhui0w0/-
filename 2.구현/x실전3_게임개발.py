from sys import stdin
N,M = map(int,stdin.readline().rstrip().split()) #맵 크기 = N x M
x,y,direction = map(int, stdin.readline().rstrip().split()) # x=캐릭터x 좌표 / y=y좌표 / direction = 보는 방향
                                                    #0=북 / 1=동 / 2=남 / 3=서

if(direction == 0):
    move_lst = [[-1,0], [0,-1], [1,0]]
elif(direction == 1):
    move_lst = [[0,1], [-1,0], [0,1]]
elif(direction == 2):
    move_lst =[[1,0], [0,1], [-1,0]]
else:
    move_lst  = [[0,-1], [1,0], [0,1]]

my_map = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)] 
    #맵은 0(육지) / 1(바다) 로 구성됨

total = 1
while(True):
    for i in range(3):
        if(my_map[x + move_lst[i][0]][y + move_lst[i][1]] == 0):
            my_map[x][y] = 1
            pre_x = x
            pre_y = y

            x = x + move_lst[i][0]
            y = y + move_lst[i][1]
            total += 1
            break
        else: #주변이 전부 바다인 경우
            x = pre_x
            y = pre_y
            
            

print(total)