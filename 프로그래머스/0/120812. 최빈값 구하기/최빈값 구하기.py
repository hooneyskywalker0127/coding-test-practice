def solution(array):
    
    count = [0] * 1000
    
    
    for num in array:
        count[num] += 1
        
    max_freq = 0      
    mode = 0          
    is_duplicate = False  
    
    for i in range(1000):
        if count[i] > max_freq:
            
            max_freq = count[i]
            mode = i
            is_duplicate = False
        elif count[i] == max_freq and max_freq != 0:
            
            is_duplicate = True
            
    
    return -1 if is_duplicate else mode