def solution(s):
    answer = ''
    sorted_s = sorted(s)
    for a in sorted_s:
        if sorted_s.count(a)==1:
            answer += a
    
    return answer


