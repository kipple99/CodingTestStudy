def solution(n):
    answer = ''
    if n % 2 == 1:
        answer = ('수박' * (n // 2)) + '수'
        
    else:
        answer = '수박' * (n//2) 
        
    return answer

print(solution(3))
print(solution(4))

####################### 모범답안 #######################

def water_melon(n):
    # 함수를 완성하세요.
    str = "수박"*n
    return str[:n]


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));

