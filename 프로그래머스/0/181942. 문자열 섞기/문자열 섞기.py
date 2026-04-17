def solution(str1, str2):
    answer = []
    
    for idx in range(len(str2)):
        answer.append(str1[idx])
        answer.append(str2[idx])
    
    
    return "".join(answer)