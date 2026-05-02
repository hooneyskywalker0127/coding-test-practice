def solution(n):
    answer = []
    i = 2
    while i <= n:
        if n % i == 0:
            if i not in answer:
                answer.append(i)
            while n % i == 0:
                n //= i
        i += 1
    
    return answer