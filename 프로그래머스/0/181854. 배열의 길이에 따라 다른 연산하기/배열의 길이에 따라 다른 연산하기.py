def solution(arr, n):
    if len(arr) % 2 == 0 :
        for a in range(1, len(arr),2):
            arr[a] += n
    else:
        for a in range(0, len(arr),2):
            arr[a] += n
    return arr