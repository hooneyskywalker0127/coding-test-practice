def solution(lines):
    answer = 0
    count = [0] * 200
    
    for line in lines:
        start, end = line
        for i in range(start+100, end +100):
            count[i] +=1
            
    for c in count:
        if c >= 2:
            answer += 1
    return answer