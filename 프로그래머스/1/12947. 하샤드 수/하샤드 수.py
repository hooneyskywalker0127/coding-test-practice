def solution(x):
    list = []
    str_x = str(x)
    for a in str_x:
        list.append(int(a))
    if int(x)% sum(list) == 0:
        return True
    elif int(x)% sum(list) != 0:
        return False
    
