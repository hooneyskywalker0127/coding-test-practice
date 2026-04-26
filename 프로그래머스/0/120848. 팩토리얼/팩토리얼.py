def solution(n):
    result = 1
    for a in range(1, 11):
        result *= a 
        if n < result:
            answer = a-1
            break
        
        elif n == result:
            answer = a
            break
    return answer