def solution(arr):
    answer = []
    for a in range(len(arr)-1):
        if arr[a] != arr[a+1]:
            answer.append(arr[a])
    
    answer.append(arr[-1])
    return answer