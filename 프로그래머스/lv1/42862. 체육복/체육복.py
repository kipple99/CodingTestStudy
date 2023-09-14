def solution(n, lost, reserve):
    # set은 공통 요소를 제거해주는 집합. 집합이기 때문에 연산 가능
    fin_reserve = set(reserve) - set(lost)
    fin_lost = set(lost) - set(reserve)

    for i in fin_reserve:
        if i - 1 in fin_lost:
            fin_lost.remove(i-1)
        elif i+1 in fin_lost:
            fin_lost.remove(i+1)
            
    answer = n - len(fin_lost)
    return answer