def solution(num_list):
    sum_2 = 0
    conv_sum = 1
    for a in num_list:
        sum_2 += a
        conv_sum *= a
    if conv_sum < sum_2**2 :
        answer = 1
    else :
        answer = 0
    return answer