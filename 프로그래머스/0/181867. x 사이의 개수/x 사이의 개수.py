def solution(myString):
    answer = []
    parts = myString.split("x")
    
    for a in parts:
        
        answer.append(len(a))
    return answer

