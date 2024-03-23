from sys import stdin
N = int(stdin.readline()) #학생수
lst = []

for i in range(N):
    data = list(map(str, stdin.readline().rstrip().split()))
    name = data[0]
    score = int(data[1])

    lst.append((name, score))

lst.sort(key = lambda x : x[1])
for i in range(N):
    print(lst[i][0],end =' ')