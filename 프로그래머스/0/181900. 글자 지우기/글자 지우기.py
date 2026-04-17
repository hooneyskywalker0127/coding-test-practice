def solution(my_string, indices):
    answer = ''
    
    for a in range(len(my_string)):
        if a in indices:
            continue
        
        answer += my_string[a]
            
    
    
    return answer