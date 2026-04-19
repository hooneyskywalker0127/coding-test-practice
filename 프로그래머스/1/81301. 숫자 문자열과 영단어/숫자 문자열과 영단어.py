def solution(s):
    my_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = []
    for a in range(len(my_list)):
        s = s.replace(my_list[a], str(a))
    
    
    return int(s)