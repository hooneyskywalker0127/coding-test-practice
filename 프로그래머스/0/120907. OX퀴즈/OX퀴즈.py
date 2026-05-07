def solution(quiz):
    answer = []
    
    for q in quiz:
        parts = q.split(' ')
        num1 = int(parts[0]) 
        num2 = int(parts[2]) 
        op = parts[1]
        num3 = int(parts[4])
        
        if op == "+":
            result = num1 + num2
        else:
            result = num1 - num2
            
        if result == num3:
            answer.append("O")
        else:
            answer.append("X")
            
    return answer
 