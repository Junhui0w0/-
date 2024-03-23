from sys import stdin
lst = ['a', 'b','c','d','e','f','g','h']
data = stdin.readline().rstrip()
location = list(data)

x = lst.index(location[0]) + 1
y = int(location[1])
#print(x,y) #디버깅

total = 0
direction = [[-2,-1], [-2,1], [2,-1],[2,1], [1,2], [1,-2], [-1,-2], [-1,2]] #총 8가지의 움직임
for i in range(8):
    if(1<= x + direction[i][0] <= 8):
        if(1<= y + direction[i][1] <= 8):
            total += 1

print(total)