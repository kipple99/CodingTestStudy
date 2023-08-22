def solution(s):
    answer = []
    count_0 = 0
    count_logic = 0

    while(s != '1'):
        count_0 += s.count('0')
        s = s.replace('0', '')
        s = len(s)
        s = bin(s)[2:]
        count_logic += 1
        
    answer.append(count_logic)
    answer.append(count_0)
    
    return answer