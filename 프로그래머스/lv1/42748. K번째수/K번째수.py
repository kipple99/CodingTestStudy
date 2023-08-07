def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0] - 1
        j = command[1]
        k = command[2] - 1
        
        temp_list = array[i:j]
        answer_list = sorted(temp_list)
        
        answer.append(answer_list[k])
        
    return answer
