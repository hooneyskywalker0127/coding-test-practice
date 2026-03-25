def solution(my_string, n):
    answer = ''
    for a in my_string:
        answer += a*n
    return answer