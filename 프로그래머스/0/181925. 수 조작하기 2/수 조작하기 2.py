def solution(numLog):
    answer = []
    
    for i in range(len(numLog) - 1):
        diff = numLog[i+1] - numLog[i]
        
        if diff == 1:
            answer.append('w')
        elif diff == -1:
            answer.append('s')
        elif diff == 10:
            answer.append('d')
        elif diff == -10:
            answer.append('a')
            
    return "".join(answer)