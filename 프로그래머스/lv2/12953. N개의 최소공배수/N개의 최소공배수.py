import math

def solution(arr):
    arr = sorted(arr)
    sol_mul = arr[0]
    for i in arr:
        sol_mul = (i * sol_mul) // math.gcd(i, sol_mul)
        
    return sol_mul