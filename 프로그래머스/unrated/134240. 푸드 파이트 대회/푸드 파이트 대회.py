def solution(food):
    answer = ''
    queue = []
    stack = []

    for i in range(1, len(food)):
        if food[i] == 1:
            pass
        
        for j in range(food[i]//2):
            queue.insert(0, str(i))
            stack.append(str(i))

    answer_list = stack + ['0'] + queue
    answer = ''.join(answer_list)
    
    return answer