from collections import deque

def solution(s):
    stack = deque()
    for i in s:
        if i == '(':
            stack.append('(')
            
        elif i == ')':
            if stack:
                stack.pop()
            else:
                return False
    # 스택에 열린 괄호 위치 데이터가 남아 있으면 해당 열린 괄호는 짝이 맞는 닫힌 괄호가 없다는 뜻이다
    while stack:
        return False

    return True

print(solution("()()")) # True
print(solution("(())()")) # True
print(solution(")()(")) # False
print(solution("(()(")) # False
