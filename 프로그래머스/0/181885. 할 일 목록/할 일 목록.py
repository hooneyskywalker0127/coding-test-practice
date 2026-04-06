def solution(todo_list, finished):
    answer = []
    for a in range(len(todo_list)):
        if finished[a] == False:
            answer.append(todo_list[a])    
    return answer