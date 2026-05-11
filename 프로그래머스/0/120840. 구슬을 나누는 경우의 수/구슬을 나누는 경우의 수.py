def solution(balls, share):
    if share > balls // 2:
        share = balls - share
        
    numerator = 1   
    denominator = 1
    
    for i in range(share):
        numerator *= (balls - i)
        denominator *= (i + 1)
        
    return numerator // denominator