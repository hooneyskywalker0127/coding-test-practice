def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        for a in range(s, e+1):
            if a%k == 0:
                arr[a] += 1
    return arr