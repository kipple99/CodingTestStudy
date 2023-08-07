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

#########################################################

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
