def solution(numbers):
    list = []
    for a in range(10):
        if a not in numbers:
            list.append(a)
    return sum(list)