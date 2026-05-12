def solution(rank, attendance):
    possible = []
    for i in range(len(rank)):
        if attendance[i]:
            possible.append((rank[i], i))
    
    possible.sort()
    
    a = possible[0][1]
    b = possible[1][1]
    c = possible[2][1]
    
    return 10000 * a + 100 * b + c