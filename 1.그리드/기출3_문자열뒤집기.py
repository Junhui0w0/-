from sys import stdin
N = stdin.readline().rstrip()
lst_0 = N.split('1') #0 뒤집기
lst_1 = N.split('0') #1 뒤집기

while(True):
    if('' not in lst_0):
        break
    lst_0.remove('')

while(True):
    if('' not in lst_1):
        break
    lst_1.remove('')

print(min(len(lst_1), len(lst_0)))