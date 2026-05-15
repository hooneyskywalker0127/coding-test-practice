def solution(keyinput, board):
    answer = []
    x_limit = board[0] // 2
    y_limit = board[1] // 2
    
    x, y = 0, 0
    
    for key in keyinput:
        if key == "left":
            # 한계를 넘지 않을 때만 이동
            if x > -x_limit:
                x -= 1
        elif key == "right":
            if x < x_limit:
                x += 1
        elif key == "up":
            if y < y_limit:
                y += 1
        elif key == "down":
            if y > -y_limit:
                y -= 1
                
    return [x, y]
    