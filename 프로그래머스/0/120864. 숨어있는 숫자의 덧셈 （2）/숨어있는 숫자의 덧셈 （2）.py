def solution(my_string):
    answer = 0
    for char in my_string:
        if not char.isdigit():
            my_string = my_string.replace(char, ' ')
    numbers = my_string.split()
    answer = sum(map(int, numbers))
    return answer