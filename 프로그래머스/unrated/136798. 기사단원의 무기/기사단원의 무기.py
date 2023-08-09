# 1 try
def solution(number, limit, power):
    measure_num = []
    answer = []
    count = 0
    
    for i in range(1, number+1):
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        measure_num.append(count)
        count = 0
    
    for measure in measure_num:
        if measure <= limit:
            answer.append(measure)
        else:
            answer.append(power)
    
    return sum(answer)


################################################

# 2 try - 공간복잡도 줄이기, 시간복잡도 O(n^2)
def solution(number, limit, power):
    answer = []
    count = 0
    
    for i in range(1, number+1):
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
                
        if count <= limit:
            answer.append(count)
            count = 0
        else:
            answer.append(power)
            count = 0
    
    return sum(answer)

################################################

# 3 try - 시간복잡도 O(n^2) * lambda 함수 사용

def solution(number, limit, power):
    answer = []
    count = 0
    for i in range(1, number+1):
        count = len(list(filter(lambda x:i%x==0, range(1, i+1))))
        
        if count <= limit:
            answer.append(count)
            count = 0
        else:
            answer.append(power)
            count = 0
    
    return sum(answer)

################################################

# 4 try
# keypoint1 : 항상 약수를 구하면 그 짝이 되는 수가 존재한다. (ex. 6 = 2 * 3)
# keypoint2 : 각각의 짝이 있으므로 제곱근보다 작은 수만큼 돌면서 반쪽을 찾고 count에 2씩 더해준다.
# keypoint3 : 제곱수의 경우 if문을 넣어 1개를 빼도록 설정. (ex. 4 * 4 경우 똑같은 수의 곱하기 이지만 count에는 2를 더했기 때문)

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

print(solution(5, 3, 2)) # 10
print(solution(10, 3, 2)) # 21
