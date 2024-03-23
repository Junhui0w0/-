from sys import stdin
N,K = map(int, stdin.readline().split())

lst_A = list(map(int, stdin.readline().rstrip().split()))
lst_B = list(map(int, stdin.readline().rstrip().split()))

for i in range(K):
    A_min = min(lst_A)
    B_max = max(lst_B)
    
    min_index = lst_A.index(A_min)
    max_index = lst_B.index(B_max)
    
    lst_A[min_index] = B_max
    lst_B[max_index] = A_min

print(sum(lst_A))