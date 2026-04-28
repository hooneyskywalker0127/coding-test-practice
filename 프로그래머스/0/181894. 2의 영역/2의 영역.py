def solution(arr):
    answer = []
    idx_list = []
    if arr.count(2) == 0:
        answer.append(-1)
    elif arr.count(2) == 1:
        answer.append(2)
    else:
        for a in range(len(arr)):
            if arr[a] == 2:
                idx_list.append(a)
        for b in range(min(idx_list),max(idx_list)+1):
            answer.append(arr[b])
    return answer