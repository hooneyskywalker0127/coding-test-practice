def solution(t, p):
    list = []
    answer = 0
    for a in range(len(t)-len(p)+1):
        list.append(int(t[a:a+len(p)]))
    
    for b in list:
        if int(p) >= b:
            answer +=1
    
    
    
    return answer