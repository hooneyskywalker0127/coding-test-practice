def solution(rny_string):
    answer = []
    for a in rny_string:
        if a != "m":
            answer.append(a)
        else:
            answer.append("rn")
    
    return "".join(answer)