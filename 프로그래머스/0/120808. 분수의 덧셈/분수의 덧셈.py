def solution(numer1, denom1, numer2, denom2):

    target_numer = (numer1 * denom2) + (numer2 * denom1)
    target_denom = denom1 * denom2
    
    
    a, b = target_numer, target_denom
    while b != 0:
        a, b = b, a % b
    gcd = a  
    
    return [target_numer // gcd, target_denom // gcd]