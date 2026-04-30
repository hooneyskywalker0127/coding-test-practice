def solution(my_str, n):
    answer = []
    for a in range(0,len(my_str),n):
        answer.append(my_str[a:a+n])
    
    
    return answer