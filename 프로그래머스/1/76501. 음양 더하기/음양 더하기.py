def solution(absolutes, signs):
    list = []
    for a in range(len(absolutes)):
        if signs[a] == True:
            list.append(absolutes[a])
        elif signs[a] == False:
            list.append(-absolutes[a])
            
    answer = sum(list)
    
    return answer