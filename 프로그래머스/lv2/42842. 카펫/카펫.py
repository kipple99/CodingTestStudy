def solution(brown, yellow):
    answer = []
    total = brown + yellow # a * b = total (총갯수 == 넓이)
    for b in range(1, total+1):
        if (total / b) % 1 == 0: # total / b = a
            a = total / b
            if a >= b:
                if 2 * a + 2 * b == brown + 4: # 2a + 2b = brwon + 4
                    return [int(a), b]
    return answer

print(solution(10, 2)) # [4, 3]
print(solution(8, 1)) # [3, 3]
print(solution(24, 24))  # [8, 6]

# 조건 
# a >= b
# yellow = (a-2)(b-2)
# brown = ab - (a-2)(b-2) = 2a + 2b - 4
