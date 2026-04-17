def solution(a, d, included):
    answer = 0
    
    for num in range(len(included)):
        if included[num] == True:
            answer += a + d*num
    
    return answer