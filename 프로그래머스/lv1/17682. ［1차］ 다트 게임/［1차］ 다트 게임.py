def solution(dartResult):
    answer = []
    formula = ''
    for i in dartResult:
        if i.isnumeric(): # isnumeric() 숫자 판별
            formula += i
        elif i == 'S':
            formula = int(formula) ** 1
            answer.append(formula)
            formula = ''
        elif i == 'D':
            formula = int(formula) ** 2
            answer.append(formula)
            formula = ''
        elif i == 'T':
            formula = int(formula) ** 3
            answer.append(formula)
            formula = ''
        
        elif i == '*':
            if len(answer) > 1:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
            else:
                answer[-1] = answer[-1] * 2
        elif i == '#':
            answer[-1] = answer[-1] * -1
    
    return sum(answer)