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

##########################################################################################

def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0) # lottos 안에 0의 갯수 찾기
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans] # 최고 등수 : (당첨갯수 + 0의갯수) / 최저 등수 : (당첨갯수)

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])) # [3, 5]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])) # [1, 6]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])) # [1, 1]
