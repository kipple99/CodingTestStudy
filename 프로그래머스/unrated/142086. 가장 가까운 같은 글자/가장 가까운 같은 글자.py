def solution(s):
    answer = []
    answer = []
    last_pos = {} # 각 문자의 마지막 위치를 저장하는 딕셔너리

    for i in range(len(s)):
        if s[i] not in last_pos:
            answer.append(-1)
        else:
            answer.append(i - last_pos[s[i]])
        last_pos[s[i]] = i
        
    return answer

# 구현 logic
# answer.append(-1) # append(-1)
# last_pos[s[0]] = 0 # {'b': 0}

# answer.append(-1) # append(-1)
# last_pos[s[1]] = 1 # {'b': 0, 'a': 1}

# answer.append(-1) # append(-1)
# last_pos[s[2]] = 2 # {'b': 0, 'a': 1, 'n': 2}

# answer.append(3 - last_pos[s[3]]) # 3 - last_pos['a](a의 딕셔너리 인덱스 값 : 2) append(2)
# last_pos[s[3]] = 3 # {'b': 0, 'a': 3, 'n': 2} 자릿값 업데이트

# answer.append(4 - last_pos[s[4]]) # 4 - last_pos['n'](n의 딕셔너리 인덱스 값 : 2) append(2)
# last_pos[s[4]] = 4 # {'b': 0, 'a': 3, 'n': 4} 자릿값 업데이트

# answer.append(5 - last_pos[s[5]]) # 5 - last_pos['a'](n의 딕셔너리 인덱스 값 : 3) append(2)
# last_pos[s[5]] = 5 # {'b': 0, 'a': 5, 'n': 4} 자릿값 업데이트