def solution(i, j, k):
    answer = 0
    str_k = str(k)
    for a in range(i,j+1):
        answer += str(a).count(str_k)
    return answer