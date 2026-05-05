def solution(dots):
    a, b, c, d = dots
    
    def is_parallel(p1, p2, p3, p4):
        y_diff1 = p2[1] - p1[1]
        x_diff1 = p2[0] - p1[0]
        y_diff2 = p4[1] - p3[1]
        x_diff2 = p4[0] - p3[0]
        
        return y_diff1 * x_diff2 == y_diff2 * x_diff1


    if is_parallel(a, b, c, d): return 1 # (A-B), (C-D)
    if is_parallel(a, c, b, d): return 1 # (A-C), (B-D)
    if is_parallel(a, d, b, c): return 1 # (A-D), (B-C)
    
    return 0