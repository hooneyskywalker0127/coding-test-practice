def solution(myString, pat):
    myString_lower = myString.lower()
    pat_lower = pat.lower()
    if pat_lower in myString_lower:
        answer = 1
    else:
        answer = 0
    return answer