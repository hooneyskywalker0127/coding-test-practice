def solution(n):
    answer_list = []
    num = 1
    while len(answer_list) < n:
        if (num % 3 != 0) and ("3" not in str(num)):
            answer_list.append(num)
        
        num += 1
    
    return answer_list[n-1]