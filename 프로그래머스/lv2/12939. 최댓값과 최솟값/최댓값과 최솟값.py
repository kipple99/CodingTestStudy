def solution(s):
    int_num = s.split(' ')
    temp = []
    
    for i in range(len(int_num)):
        t = int(int_num[i])
        temp.append(t)

    answer = str(min(temp)) + ' ' + str(max(temp))
        
    return answer