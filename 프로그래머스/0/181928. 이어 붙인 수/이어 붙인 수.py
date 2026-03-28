def solution(num_list):
    odd = []
    even = []
    
    for a in num_list:
        if a % 2 == 0:
            even.append(str(a))
        else:
            odd.append(str(a))
            
    answer = int("".join(even)) + int("".join(odd))
    return answer