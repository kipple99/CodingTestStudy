def solution(a, b, n):
    cola = 0
    remain = 0

    while(n >= a):
        remain = n % a
        cola += b*(n//a)
        n = b*(n//a)
        n += remain
        
    return cola