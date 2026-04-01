def solution(hp):
    answer = 0
    general_ant = hp // 5
    soldier_ant = hp % 5 // 3
    normal_ant = hp % 5 % 3// 1
    answer = general_ant+soldier_ant+normal_ant
    return answer