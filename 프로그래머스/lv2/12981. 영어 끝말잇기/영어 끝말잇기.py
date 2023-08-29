def solution(n, words):
    used_words = []
    used_words.append(words[0])
    last_word = used_words[0][-1]
    number, order = 0, 0
    
    for i in range(1, len(words)):
        if words[i] not in used_words and last_word == words[i][0]:
            used_words.append(words[i])
            last_word = words[i][-1]
        else:
            number = (i % n) + 1 # 먼저 탈락하는 사람의 번호
            order = (i // n) + 1 # 자신의 몇번째 차례 탈락?
            break
    
    return [number, order]