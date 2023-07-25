def solution(n, arr1, arr2):
    answer = []
    arr1_list = []
    arr2_list = []
    temp_1 = ''

    
    # 파이썬 내장함수 bin() 이용 
    # ex) bin(9) -> '0b1001'
    # bin(9)[2:] -> '1001
    
    
    for i in arr1:
        temp = bin(i)[2:]
        while len(temp) < n:
            temp = '0' + temp
        arr1_list.append(temp)
        
    for i in arr2:
        temp = bin(i)[2:]
        while len(temp) < n:
            temp = '0' + temp
        arr2_list.append(temp)
        
    ##############################################
        
    for i in range(n):
        for j in range(n):
            if (arr1_list[i][j] == '0' and arr2_list[i][j] == '0'):
                temp_1 += ' '
            else:
                temp_1 += '#'
                
        answer.append(temp_1)
        temp_1 = ''
            
    
    return answer