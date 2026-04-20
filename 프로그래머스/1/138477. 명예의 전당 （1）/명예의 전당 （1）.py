def solution(k, score):
    hof = [] 
    answer = []
    
    
    for a in score:
        if len(hof)<k:
            hof.append(a)
            hof.sort()
            answer.append(hof[0])
        else:
            hof.append(a)
            hof.sort()
            del hof[0]
            answer.append(hof[0])
    
    return answer