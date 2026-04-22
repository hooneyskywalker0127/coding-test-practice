def solution(num_list, n):
    answer = []
    idx = 0
    while idx < len(num_list):
        answer.append(num_list[idx:idx+n])
        idx += n
    
    
    return answer