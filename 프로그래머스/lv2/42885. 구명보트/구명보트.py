from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))

    while len(people) >= 2:
        if people[0] + people[-1] <= limit: # 제일 뚱뚱한 사람과 날씬한 사람의 합이 limit 보다 작다면
            # 두명 묶어서 보트 태워서 내보냄
            people.pop() # 제일 뚱뚱한 사람 pop()
            people.popleft() # 제일 날씬한 사람 popleft() == pop(0)
            answer += 1
            
        else:
            people.pop()
            answer += 1
    
    if len(people) == 1: # 한명 남으면 그 한사람 내보내고 종료 
            answer += 1
            
    return answer