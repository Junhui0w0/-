from sys import stdin
from collections import Counter

N, M, K = map(int, stdin.readline().rstrip().split())
    #N = 숫자 개수 // M = 덧셈 횟수 // K = 최대 반복 횟수

lst = list(map(int, stdin.readline().split()))

lst.sort()


first_value = lst[-1]
second_value = lst[N-2]
#print(first_value, second_value) #디버깅

cnt = 1
total = 0
while(True):
    if(M < K):
        if(cnt % 2 == 1):
            total += first_value * M
        else:
            total += second_value
        #print(total) #디버깅
        break
    else:
        if(cnt % 2 == 1):
            total += first_value * K
            M = M - K
        else:
            total += second_value
            M = M - 1
        cnt += 1
    #print(total) #디버깅

print(total)