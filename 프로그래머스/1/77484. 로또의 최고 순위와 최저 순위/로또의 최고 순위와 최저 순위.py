def solution(lottos, win_nums):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]
    zero_count = lottos.count(0)
    answer_count = len(set(lottos) & set(win_nums))

    answer.append(rank[zero_count + answer_count])
    answer.append(rank[answer_count])
    
    return answer
