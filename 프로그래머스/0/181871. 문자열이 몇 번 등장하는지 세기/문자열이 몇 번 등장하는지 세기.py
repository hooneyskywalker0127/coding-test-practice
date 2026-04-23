def solution(myString, pat):
    answer = 0
    for a in range(len(myString)):
        if myString[a:a+len(pat)] == pat :
            answer +=1
    
    return answer

