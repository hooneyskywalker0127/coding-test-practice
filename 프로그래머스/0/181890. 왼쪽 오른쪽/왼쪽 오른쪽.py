def solution(str_list):
    answer = []
    
    for a in range(len(str_list)):
        if str_list[a] == 'l':
            return str_list[:a]
        elif str_list[a] == 'r':
            return str_list[a+1:]
    return []


