from collections import Counter

def solution(k, tangerine):
    answer = 0

    counter=Counter(tangerine)
    sort_counter = sorted(counter.items(),key=lambda x:x[1],reverse=True)

    # 정렬된 딕셔너리로 귤 개수 맞추기
    for i in sort_counter:
        k -= i[1]
        answer += 1

        if k <= 0:
            break

    return answer