def solution(num_list, n):
    answer = []
    for a in num_list[n:]:
        answer.append(a)
    
    for b in num_list[:n]:
        answer.append(b)
    
    return answer