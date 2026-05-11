def solution(sides):
    answer = 0
    max_val = max(sides)
    min_val = min(sides)
    
    for a in range(max_val - min_val + 1, max_val + 1):
        answer += 1

    for a in range(max_val + 1, max_val + min_val):
        answer += 1
        
    return answer