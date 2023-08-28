def solution(brown, yellow):
    answer = []
    total = brown + yellow # a * b = total (총갯수 == 넓이)
    for b in range(1, total+1):
        if (total / b) % 1 == 0: # total / b = a
            a = total / b
            if a >= b:
                if 2 * a + 2 * b == brown + 4: # 2
                    return [int(a), b]
    return answer