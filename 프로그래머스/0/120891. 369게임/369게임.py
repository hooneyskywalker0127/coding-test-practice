def solution(order):
    answer = 0
    order = str(order)
    
    for char in order:
        if char == '3' or char == '6' or char == '9':
            answer +=1
        
    return answer