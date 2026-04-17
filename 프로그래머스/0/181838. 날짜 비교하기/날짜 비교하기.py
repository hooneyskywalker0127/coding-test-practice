def solution(date1, date2):
    a = 0
    while a < len(date1):
        if date1[a] < date2[a]:
            return 1
        elif date1[a] > date2[a]:
            return 0
        a +=1
        
    return 0
    