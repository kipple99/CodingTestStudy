def solution(A,B):
    answer = 0
    list_1 = sorted(A)
    list_2 = sorted(B, reverse=True)
    
    for i in range(len(list_1)):
        answer += list_1[i] * list_2[i]


    return answer