def solution(x, n):
    answer = []
    for a in range(n):
        answer.append(x+x*a)
    
    return answer