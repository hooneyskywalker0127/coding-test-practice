def solution(s, n):
    low = 'abcdefghijklmnopqrstuvwxyz'
    up = low.upper()
    answer = []
    
    for char in s:
        if char == ' ':
            answer.append(' ')
        elif char in low:
            
            idx = low.find(char)
    
            new_idx = (idx + n) % 26
            answer.append(low[new_idx])
        elif char in up:
            idx = up.find(char)
            new_idx = (idx + n) % 26
            answer.append(up[new_idx])
            
    return "".join(answer)