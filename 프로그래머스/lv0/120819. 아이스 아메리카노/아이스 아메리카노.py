def solution(money):
    
    count = money // 5500
    rest = money % 5500
    answer = [count,rest]
    return answer