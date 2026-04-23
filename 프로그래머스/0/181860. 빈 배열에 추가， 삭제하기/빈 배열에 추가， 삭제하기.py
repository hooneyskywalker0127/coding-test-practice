def solution(arr, flag):
    answer = []
    for a in range(len(arr)):
        if flag[a] == True:
            answer.extend([arr[a]] * (arr[a] * 2))
        
        else:
            del answer[-arr[a]:]
    return answer