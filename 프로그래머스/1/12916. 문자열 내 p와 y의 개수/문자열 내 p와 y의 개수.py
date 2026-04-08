def solution(s):
    
    p_list = []
    y_list = []
    
    lower_s = s.lower()
    for string in lower_s:
        if string == "p":
            p_list.append(string)
        elif string == "y":
            y_list.append(string)
    if len(p_list) == len(y_list):
        return True
    
    else:
        return False 
    
    
    