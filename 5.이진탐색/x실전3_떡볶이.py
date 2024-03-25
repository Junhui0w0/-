from sys import stdin
N, M = map(int, stdin.readline().split()) #N = 떡 개수 / M = 손님이 가져갈 떡의 최소 길이
lst = list(map(int, stdin.readline().rstrip().split())) #떡 list

def search(lst):
    while(True):
        lst.sort()
        H = ((lst[0] + lst[-1]) // 2) #가장 작은 길이 + 가장 긴 길이
        
        total = 0
        for i in lst:
            if(i > H):
                total += i-H 
            
        if(total > M):
            lst[-1] = H
        elif(total < M):
            lst[0] = H
        else:
            return H
        print(lst)

print(search(lst))