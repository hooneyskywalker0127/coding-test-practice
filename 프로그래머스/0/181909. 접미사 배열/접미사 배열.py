def solution(my_string):
    answer = []
    for a in range(len(my_string)):
        answer.append(my_string[a:])
    answer.sort()
    return answer