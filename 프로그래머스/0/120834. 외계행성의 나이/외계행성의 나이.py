def solution(age):
    answer_list = []
    age_str = str(age)
    alphabet = ['a','b','c','d','e','f','g','h','i','j']
    
    for digit in age_str:
        index = int(digit)
        answer_list.append(alphabet[index])
        
    answer = "".join(answer_list)
    return answer