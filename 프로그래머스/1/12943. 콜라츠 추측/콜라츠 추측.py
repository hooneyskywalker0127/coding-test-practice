def solution(num):
    n = 0
    while num != 1 and n < 500:
        n  += 1
        if num % 2==0:
            num //= 2
        else:
            num = num*3 +1
        
    return n if num == 1 else -1

