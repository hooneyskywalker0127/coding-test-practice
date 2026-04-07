def solution(n):
    answer = []
    
    s = str(n)
    
    reversed_s = s[::-1]
    
    for a in reversed_s:
        answer.append(int(a))
    
    return answer