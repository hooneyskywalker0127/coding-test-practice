def solution(s1, s2):
    answer = []
    for a in s1:
        for b in s2:
            if b== a :
                answer.append(a)
    return len(answer)

