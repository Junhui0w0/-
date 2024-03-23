from sys import stdin
N = int(stdin.readline()) #동전 갯수
coin_lst = list(map(int, stdin.readline().rstrip().split()))
sum_lst= list() #각 코인별 합계

for i in range(0,N):
    total = 0
    for j in range(i,N):
        total += coin_lst[j]
        if(total not in sum_lst):
            sum_lst.append(total)

#print(sum_lst) #디버깅

min_coin = min(sum_lst)
plus = 1

while(True):
    if(min_coin + plus not in sum_lst):
        print(min_coin + plus)
        break
    else:
        plus += 1

