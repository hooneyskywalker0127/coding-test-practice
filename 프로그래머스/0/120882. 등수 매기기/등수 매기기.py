def solution(score):
    sum = [a+b for a,b in score]
    
    sorted_sum = sorted(sum, reverse = True)
    answer = []
    
    for s in  sum:
        answer.append(sorted_sum.index(s)+1)
    
    
    return answer