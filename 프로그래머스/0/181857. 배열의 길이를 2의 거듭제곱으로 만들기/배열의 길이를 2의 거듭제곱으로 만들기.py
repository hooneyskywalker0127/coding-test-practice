def solution(arr):
    answer = []
    for a in range(len(arr)):
        answer.append(arr[a])
    target = 1
    while len(arr) > target:
        target *= 2
    while len(answer) < target:
        answer.append(0)
    
    return answer