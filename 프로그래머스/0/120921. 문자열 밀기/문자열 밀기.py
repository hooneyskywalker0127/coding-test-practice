def solution(A, B):
    if A == B:
        return 0
    
    current_A = A
    
    for i in range(1, len(A) + 1):
        current_A = current_A[-1] + current_A[:-1]
        
        if current_A == B:
            return i
            
    return -1 