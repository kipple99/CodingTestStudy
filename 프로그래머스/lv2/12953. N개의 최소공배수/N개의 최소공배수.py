import math

def solution(arr):
    arr = sorted(arr)
    result_gcd = arr[0]
    new_arr = [] 
    answer = 1

    for i in arr[1:]:
        result_gcd = math.gcd(result_gcd, i)
    
    for j in arr:
        new_arr.append(j // result_gcd)
        
    for k in new_arr:
        answer *= k
        
    answer *= result_gcd
    
    return answer

# 모범답안
def solution(arr):
    arr = sorted(arr)
    sol_mul = arr[0]
    for i in arr:
        sol_mul = (i * sol_mul) // math.gcd(i, sol_mul)
        
    return sol_mul
