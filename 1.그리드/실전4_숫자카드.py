from sys import stdin
N,K = map(int,stdin.readline().split())

total = 0
while(N != 1):
    if(N % K == 0):
        N = N / K
        total += 1
    else:
        N = N - 1
        total += 1

print(total)