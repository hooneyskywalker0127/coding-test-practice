def solution(my_strings, parts):
    answer = []
    
    for i in range(len(my_strings)):
        string = my_strings[i]
        s, e = parts[i] 
        
        
        part_str = string[s : e + 1]
        
        
        answer.append(part_str)
    
    return "".join(answer)