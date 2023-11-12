def solution(babbling):
    answer = 0
    bab_sentence = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in bab_sentence:
            if j*2 not in i: # 옹알이 사전에 반복되는 값이 있는지 판단
                i = i.replace(j, ' ') # 공백으로 바꿈
                
        if len(i.replace(' ', '')) == 0: # 공백을 없앴을때, 길이가 0이면
            answer += 1
    return answer