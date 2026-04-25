def solution(strArr):
    strArr_list = []
    answer = []
    for a in strArr:
        strArr_list.append(len(a))
    
    for b in range(max(strArr_list)+1):
        answer.append(strArr_list.count(b))
        
    
    
    return max(answer)