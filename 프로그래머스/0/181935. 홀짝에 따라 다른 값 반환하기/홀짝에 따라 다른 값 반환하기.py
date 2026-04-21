def solution(n):
    answer = 0
    if n%2 != 0:
        for a in range(1,n+1):
            if a%2 != 0:
                answer += a
    else:
        for b in range(1,n+1):
            if b%2 == 0:
                answer += b**2
        
        
    return answer