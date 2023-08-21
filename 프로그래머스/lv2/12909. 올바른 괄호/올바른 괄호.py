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
    while stack:
        return False

    return True