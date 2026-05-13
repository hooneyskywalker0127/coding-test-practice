def solution(id_pw, db):
    answer = ''
    
    for a,b in db:
        if id_pw[0] == a:
            if id_pw[1] == b:
                return 'login'
            else:
                return 'wrong pw'
        

    return 'fail'