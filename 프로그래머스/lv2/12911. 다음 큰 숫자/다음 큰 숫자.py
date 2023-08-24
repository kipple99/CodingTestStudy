def solution(n):
    answer = 0
    bin_n = bin(n)[2:]
    t = n + 1

    if bin_n.count('0') == 0:
        bin_n = bin_n[:1] + '0' + bin_n[1:]
        answer = int(bin_n, 2)


    while(t > n):
        bin_t = bin(t)[2:]
        if bin_t.count('1') == bin_n.count('1'):
            answer = int(bin_t,2)
            break
        else:
            t += 1
            
    return answer