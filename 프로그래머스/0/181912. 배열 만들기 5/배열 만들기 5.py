def solution(intStrs, k, s, l):
    answer = []
    for a in range(len(intStrs)):
        if k < int(intStrs[a][s:s+l]):
            answer.append(int(intStrs[a][s:s+l]))
    
    return answer