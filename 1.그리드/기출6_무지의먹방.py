from sys import stdin

def solution(food_times, k): #food_times = 리스트 // K= 지연시간
    answer = 0

    print(food_time_lst)

    index = 0
    for i in range(k):
        while(True):
            if(food_times[index] == 0):
                index += 1
            else:
                break
        food_times[index] = food_times[index] - 1
        index += 1
        if(index == len(food_times)):
            index = 0

    for i in range(k):
        if food_times[i] != 0:
            answer = i+1
            break

    return answer


delay_time = int(stdin.readline())
food_time_lst = list(map(int, stdin.readline().rstrip().split()))
print(solution(food_time_lst, delay_time))