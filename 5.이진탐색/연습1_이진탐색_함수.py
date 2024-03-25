from sys import stdin
N, M = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().rstrip().split()))
lst.sort()

def search(lst, target, start, end):
    while(start <= end):
        mid = (start + end) // 2
        
        if(lst[mid] == target):
            return mid
        elif(lst[mid] > target):
            end = mid -1
        elif(lst[mid] < target):
            start = mid + 1
    return None

res =search(lst, M, 0, N)
if(res == None):
    print("해당 원소 없음")
else:
    print(res + 1,'번째에 해당 원소 존재')