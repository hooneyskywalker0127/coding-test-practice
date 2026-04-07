def solution(n):
    answer = 0
    s = n**(1/2)
    
    if s%1 == 0:
        answer = (s+1)**2
    else:
        answer = -1
    
    return answer