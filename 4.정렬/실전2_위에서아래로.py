from sys import stdin
N = int(stdin.readline())

lst = [0] * N
for i in range(N):
    lst[i] = int(stdin.readline().rstrip())

lst.sort(reverse=True)
print(*lst)