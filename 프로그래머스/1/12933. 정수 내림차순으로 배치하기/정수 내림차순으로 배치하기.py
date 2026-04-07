def solution(n):
    s = list(str(n))
    s.sort(reverse = True)
    answer = "".join(s)
    
    return int(answer)



