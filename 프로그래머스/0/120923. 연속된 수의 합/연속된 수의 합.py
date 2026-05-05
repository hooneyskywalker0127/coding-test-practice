def solution(num, total):
    
    start = (total - sum(range(num))) // num
    
    return [i for i in range(start, start + num)]