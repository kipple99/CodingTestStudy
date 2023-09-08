def solution(name, yearning, photo):
    answer = []
    dictionary = dict(zip(name, yearning))
    
    for i in photo:
        name_sum = 0
        for j in range(len(i)):
            if i[j] in dictionary:
                name_sum += dictionary[i[j]]
        answer.append(name_sum)
    return answer