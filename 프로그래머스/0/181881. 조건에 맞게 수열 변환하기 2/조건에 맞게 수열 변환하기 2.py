def solution(arr):
    answer = 0
    
    while True:
        next_arr = []
        
        for a in arr:
            if a >= 50 and a % 2 == 0:
                next_arr.append(a // 2)
            elif a < 50 and a % 2 != 0:
                next_arr.append(a * 2 + 1)
            else:
                next_arr.append(a)
                
            if arr == next_arr :
                return answer
        arr = next_arr
        answer += 1
        
        