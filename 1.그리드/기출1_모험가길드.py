from sys import stdin
N = int(stdin.readline())
lst = list(map(int, stdin.readline().rstrip().split()))
lst.sort()

group = 0 #꾸릴 수 있는 그룹 수
member_count = 0 #한 그룹에 있는 인원수
for i in lst:
    member_count += 1
    if member_count >= i:
        group += 1
        member_count = 0

print(group)