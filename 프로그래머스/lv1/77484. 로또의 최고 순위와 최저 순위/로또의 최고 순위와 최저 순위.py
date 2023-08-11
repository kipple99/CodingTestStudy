def solution(lottos, win_nums):
    max_count = 0
    min_count = 0
    answer = []

    for i in lottos:
        if i == 0:
            max_count += 1
        elif i in win_nums:
            max_count += 1
            min_count += 1


    def rank_num(count):
        if count == 6:
            rank = 1

        elif count == 5:
            rank = 2
            
        elif count == 4:
            rank = 3
            
        elif count == 3:
            rank = 4
            
        elif count == 2:
            rank = 5
            
        else:
            rank = 6
        
        return rank
    
    answer.append(rank_num(max_count))
    answer.append(rank_num(min_count))
    
    return answer