def solution(num_list):
    for a in range(len(num_list)):
        if num_list[a] < 0:
            return a
    return -1