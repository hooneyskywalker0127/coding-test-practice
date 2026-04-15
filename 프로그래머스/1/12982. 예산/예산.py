def solution(d, budget):
    sorted_d = sorted(d)
    list = []
    
    
    for a in sorted_d:
        if sum(list) <= budget:
            list.append(a) 
        if sum(list) > budget:
            list.pop()
            
    
    
    return len(list)