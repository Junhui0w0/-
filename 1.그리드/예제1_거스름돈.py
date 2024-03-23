from sys import stdin

N = int(stdin.readline().rstrip()) #거슬러 줄 금액 == 10의 배수
coin_lst = [500, 100, 50, 10]

total = 0
for i in coin_lst:
    if(N // i):
        total += N // i
        N = N - (i * (N // i))

print(total)