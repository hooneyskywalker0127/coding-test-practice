def solution(arr):
    if len(arr) ==1 or len(arr)==0:
        return [-1]
    else:
        arr.remove(min(arr))
        return arr
    