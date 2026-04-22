def solution(my_string):
    answer = []
    for a in my_string:
        if a not in answer:
            answer.append(a)
        else:
            continue
            
    
    return "".join(answer)