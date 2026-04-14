def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer.append(numbers[-1])
        for a in range(len(numbers)-1):
            answer.append(numbers[a])
            
    elif direction == "left":
        for a in range(1,len(numbers)):
            answer.append(numbers[a])
        answer.append(numbers[0])
    return answer