def solution(A,B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=False)
    
    for a in range(len(A)):
        answer += A[a] * B[a]
    
    return answer