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

### 다른 사람의 코드

def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])) # [3, 3]
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])) # [0, 0]
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])) # [1, 3]
