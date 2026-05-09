def solution(my_string):
    answer = [0] *52
    
    for char in my_string:
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')
            answer[index] += 1
        elif 'a' <= char <= 'z':
            index = ord(char) - ord('a') + 26
            answer[index] += 1
    return answer