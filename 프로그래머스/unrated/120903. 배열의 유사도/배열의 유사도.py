def solution(s1, s2):
    answer = 0
    
    for i in s1:
        for j in s2:
            if i == j:
                answer += 1
    
    return answer

def solution(s1, s2):
    return len(set(s1)&set(s2))