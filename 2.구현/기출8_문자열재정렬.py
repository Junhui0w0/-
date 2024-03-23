from sys import stdin
N = list(map(str, stdin.readline().rstrip()))
#알파벳 A ~ Z => 65 ~ 90

ans = []
total = 0
for i in N:
    if(65 <= ord(i) <= 90):
        ans.append(i)
    else:
        total += int(i)

ans.sort()
print(*ans,total,sep='')