def solution(s):

    list = []
    str = s.split()
    for a in str:
        list.append(int(a))
        
    max_list = max(list)
    min_list = min(list) 
    answer = f'{min_list} {max_list}'
    
    return answer