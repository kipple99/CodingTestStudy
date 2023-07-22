def solution(strings, n):
    answer = []
    answer = sorted(strings, key=lambda x:x[n]) # x[n]을 기준으로 정렬하고, 같을 경우 사전 순으로 앞선 문자열로 정리하기
    
    return answer

print(solution(['sun', 'bed', 'car'], 1))
print(solution(['abce', 'abcd', 'cdx'], 2))