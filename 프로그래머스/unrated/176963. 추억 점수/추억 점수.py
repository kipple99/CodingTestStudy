def solution(name, yearning, photo):
    answer = []
    dictionary = dict(zip(name, yearning))
    answer = []
    name_sum = 0
    
    for i in photo:
        for j in range(len(i)):
            if i[j] in dictionary:
                name_sum += dictionary[i[j]]
            else:
                pass
        answer.append(name_sum)
        name_sum = 0
    return answer
