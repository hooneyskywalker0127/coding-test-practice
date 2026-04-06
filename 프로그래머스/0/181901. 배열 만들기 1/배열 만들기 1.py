def solution(n, k):
    answer = []
    for a in range(k,n+1,k):
        answer.append(a)
    return answer