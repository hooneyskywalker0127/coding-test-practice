def solution(before, after):
    sorted_before = sorted(before)
    sorted_after = sorted(after)
    if sorted_before == sorted_after:
        answer = 1
    else:
        answer = 0
    
    return answer