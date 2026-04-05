def solution(num_list):
    
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        mul = 1
        for a in num_list:
            mul *= a 
        return mul
 
