def solution(common):
    
    if common[2] - common[1] == common[1] - common[0]:
        add = common[1] - common[0]
        answer = common[-1] + add
        return answer
    else:
        multi = common[1] // common[0]
        answer = common[-1] * multi
        return answer