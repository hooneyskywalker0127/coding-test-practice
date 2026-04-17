def solution(num_list):
    answer = 0
    
    for a in num_list:
        while a > 1:
            if a%2 ==0:
                a= a/2
            else:
                a= (a-1)/2
            answer +=1
        
    return answer