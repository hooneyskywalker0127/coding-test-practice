def solution(cipher, code):
    answer = ''
    for char in range(0,len(cipher)):
        if (char+1) % code == 0:
            answer += cipher[char]
    return answer


