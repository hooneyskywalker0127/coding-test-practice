def solution(s):
    s_split = s.split(' ')
    answer = 0
    for a in range(len(s_split)):
        if s_split[a] != 'Z':
            answer += int(s_split[a])
        elif s_split[a] == 'Z':
            answer -= int(s_split[a-1])
    return answer