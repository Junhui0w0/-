from sys import stdin
N = int(stdin.readline())
N_lst = list(map(int, stdin.readline().rstrip().split()))
N_lst.sort()

M = int(stdin.readline())
M_lst = list(map(int, stdin.readline().rstrip().split()))
M_lst.sort()

def search(lst, target, start, end):
    while(True):
        mid = (start + end) // 2

        if(start > end):
            return print('no', end=' ')
        else:
            if(lst[mid] == target):
                return print('yes', end=' ')
            elif(lst[mid] > target):
                end = mid - 1
            else:
                start = mid + 1

for i in M_lst:
    search(N_lst, i, 0, N)