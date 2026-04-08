def solution(n):
    list = []
    
    for a in range(1,n):
        if n%a ==1:
            list.append(a)
            if len(list) == 1:
                answer = a
    return answer