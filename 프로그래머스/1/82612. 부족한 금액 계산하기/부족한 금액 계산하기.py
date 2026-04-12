def solution(price, money, count):
    process = 0
    for a in range(1,count+1):
        process -= price*a
    if process + money < 0:    
        answer = abs(process + money)
    else:
        answer = 0
    return answer