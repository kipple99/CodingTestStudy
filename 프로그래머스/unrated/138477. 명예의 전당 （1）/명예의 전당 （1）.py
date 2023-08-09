def solution(k, score):
    answer = []
    ranking = []
    for i in range(len(score)):
        ranking.append(score[i])
        if len(ranking) <= k:
            answer.append(min(ranking))
        else:
            ranking.remove(min(ranking))
            answer.append(min(ranking))
            
    return answer