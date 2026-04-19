def solution(numbers):
    num_list = []
    n = len(numbers)
    
    for a in range(n):
        for b in range(a+1,n):
            num_list.append(numbers[a]+numbers[b])
    
    answer = sorted(list(set(num_list)))
    
    return answer