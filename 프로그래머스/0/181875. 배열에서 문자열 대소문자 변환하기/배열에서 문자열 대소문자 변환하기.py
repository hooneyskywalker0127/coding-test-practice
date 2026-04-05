def solution(strArr):
    answer = []
    for a in range(len(strArr)):
        if a % 2 == 0:
            answer.append(strArr[a].lower())
        else:
            answer.append(strArr[a].upper())
    return answer