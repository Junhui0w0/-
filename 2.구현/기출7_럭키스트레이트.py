from sys import stdin
N = list(map(int, stdin.readline().rstrip())) #숫자 입력
half_len = int(len(N)/2)


first_hap = 0
for i in range(0,half_len):
    first_hap += N[i]

second_hap = 0
for i in range(half_len,len(N)):
    second_hap += N[i]

if(first_hap == second_hap):
    print("LUCKY")
else:
    print("READY")