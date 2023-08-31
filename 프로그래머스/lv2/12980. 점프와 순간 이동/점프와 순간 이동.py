def solution(n):
    ans = 0
    while(n > 0):
        if n % 2 == 1: # jump(배터리 소모 o) 
            n -= 1
            ans += 1
        elif n % 2 == 0: # 순간이동(배터리 소모 X) 2의 배수
            n = n // 2
    
    return ans

print(solution(5)) # 2
print(solution(6)) # 2
print(solution(5000)) # 5
