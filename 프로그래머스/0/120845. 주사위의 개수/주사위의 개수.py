def solution(box, n):
    width_count = box[0] // n
    length_count = box[1] // n
    height_count = box[2] // n
    answer = width_count * length_count * height_count
    return answer