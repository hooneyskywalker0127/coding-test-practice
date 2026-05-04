def solution(n):
    
    is_prime = [True] * (n + 1)
    
    
    is_prime[0] = is_prime[1] = False
    
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]: # i가 소수인 경우
            
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
                
    
    return is_prime.count(True)