def solution(babbling):
    answer = 0
    possible = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        for j in possible:
            if j*2 not in i: # 문자열이 연속하여 나오는지 체크하기
                i = i.replace(j, ' ') # 만약 옹알이 할 수 있는 단어가 중복해서 나오지 않으면 단어들을 공백으로 변환
        
        if len(i.strip()) == 0: # 이렇게 옹알이 단어들에 대해 모두 변환 후 공백을 제거 했을때, 길이가 0이면 모두 발음할 수 있는 단어로 판단
            answer += 1
    return answer