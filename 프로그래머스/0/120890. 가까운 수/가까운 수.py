def solution(array, n):
    array.sort()
    er_list = []
    for a in array:
        er_list.append(abs(a - n))
    
    
    idx = er_list.index(min(er_list))
    
    return array[idx]


