def solution(number, limit, power):
    answer = []
    count = 0
    
    for i in range(1, number+1):
        count = 0
        for j in range(1, int(i**(1/2))+1):
            if(i % j == 0):
                count += 2
                if j**2 == i: # 제곱수 경우 -1
                    count -= 1
            if count > limit: # limit값을 초과하면 power 값으로 return
                count = power
                break
        answer.append(count)
        
    return sum(answer)