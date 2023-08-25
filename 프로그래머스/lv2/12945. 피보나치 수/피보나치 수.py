def solution(n):
    answer = 0
    fib_table = [0,1,1]
    
    if n > 2:
        for i in range(3, n+1):
            fib_sum = fib_table[i-1] + fib_table[i-2]
            fib_table.append(fib_sum)
    
    answer = fib_table[n] % 1234567
    
    return answer