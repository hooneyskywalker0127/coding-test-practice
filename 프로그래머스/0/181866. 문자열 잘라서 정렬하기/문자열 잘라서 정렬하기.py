def solution(myString):
    answer = []
    
    myString_split = myString.split('x')
    for a in myString_split:
        if a != "":
            answer.append(a)
    answer.sort()
    return answer