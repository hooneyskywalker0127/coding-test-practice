def solution(polynomial):
    polynomial_split = polynomial.split(' + ')
    x_sum = 0
    con_sum = 0
    
    for a in polynomial_split:
        if 'x' in a:
            if a == 'x':
                x_sum += 1
            else:
                x_sum += int(a.replace('x',' '))
        else:
            con_sum += int(a)
                
    result = []
    
    if x_sum > 0:
        if x_sum == 1:
            result.append("x")
        else:
            result.append(f"{x_sum}x")
    
    if con_sum > 0:
        result.append(str(con_sum))
    
    return " + ".join(result)