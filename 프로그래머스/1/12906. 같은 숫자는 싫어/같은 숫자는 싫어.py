from collections import deque

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == len(arr)-1:
            answer.append(arr[i])
            break
        else:
            answer.append(arr[i])
            if arr[i] == arr[i+1]:
                answer.pop()
    
    return answer