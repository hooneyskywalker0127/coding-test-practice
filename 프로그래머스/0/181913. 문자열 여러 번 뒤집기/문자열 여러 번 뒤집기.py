def solution(my_string, queries):
    
    answer = list(my_string)
    
    for a,b in queries:
        answer[a:b+1] = answer[a:b+1][::-1]
    
    
    
    return "".join(answer)