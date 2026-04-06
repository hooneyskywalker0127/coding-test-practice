def solution(num_list):
    even = 0
    odd = 0
    for a in range(len(num_list)):
        if a%2 == 0:
            even += num_list[a]
        else:
            odd += num_list[a]
            
    if odd > even :
        answer = odd
    else:
        answer = even
    
    return answer