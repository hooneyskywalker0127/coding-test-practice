def solution(myString, pat):
    inverse = ''
    for a in myString:
        if a == 'A':
            inverse += 'B'
        else:
            inverse += 'A'
    
    if pat in inverse:
        return 1
    else:
        return 0