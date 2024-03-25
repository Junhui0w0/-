from sys import stdin
N, M = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().rstrip().split()))
lst.sort()

start = 0
end = N
while(True):
    mid = (start + end) // 2
    if(start > end):
        print("해당 원소 존재x")
        break
    else:
        if(lst[mid] == M):
            print(mid + 1,'번째에 해당 원소 존재')
            break
        elif(lst[mid] > M):
            end = mid - 1
        else:
            start = mid + 1
