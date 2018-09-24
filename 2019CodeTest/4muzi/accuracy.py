def solution(food_times, k):
    # if food is consumed up
    if sum(food_times) <= k :
        return -1
    
    size = len(food_times)
    cnt = 0
    while food_times[cnt] == 0:
        cnt += 1
        cnt %= size
    
    while k > 0:
        food_times[cnt] -= 1
        k -= 1
        
        cnt += 1
        cnt %= size
        while food_times[cnt] == 0:
            cnt += 1
            cnt %= size
        # print(food_times)
    
    # print (cnt)
    
    answer = cnt + 1
    return answer
