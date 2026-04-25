def solution(myStr):
    replaced = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ')
    answer = replaced.split()
    
    return answer if answer else ["EMPTY"]