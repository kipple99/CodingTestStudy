# 시간 초과
def solution(X, Y):
    X = list(X)
    Y = list(Y)
    str_list = []

    for i in X:
        if i in Y:
            str_list.append(i)
            del Y[Y.index(i)]
    
    if str_list:
        answer_list = sorted(str_list, reverse=True)
        if answer_list[0] == '0':
            answer = '0'
            return answer
        answer = ''.join(answer_list)
    else:
        answer = '-1'

    return answer

########################################################################
# 모범답안
def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '':
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer


print(solution('100', '2345')) # '-1'
print(solution('100', '203045')) # '0'
print(solution('100', '123450')) # '10'
print(solution('12321', '42531')) # '321'
