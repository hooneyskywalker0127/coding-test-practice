def solution(number):
    list = []
    
    for a in number:
        list.append(int(a))
    sum_list = sum(list)
    
    answer = sum_list%9
    
    
    return answer