def solution(strings, n):
    for x in strings:
        strings.sort(key=lambda x: (x[n], x))
    return strings