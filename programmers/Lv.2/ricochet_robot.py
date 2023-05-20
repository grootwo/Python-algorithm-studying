def solution(board):
    check = False
    for i in range(len(board)):
        if check is True:
            break
        for j in range(len(board[0])):
            if board[i][j] == "R":
                now_r = i
                now_c = j
                check = True
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    can_arrive = False
    for i in range(len(board)):
        if can_arrive is True:
            break
        for j in range(len(board[0])):
            if board[i][j] == "G":
                for k in range(4):
                    next_r = i + dx[k]
                    next_c = j + dy[k]
                    if 0 <= next_r < len(board) and 0 <= next_c < len(board[0]):
                        if board[next_r][next_c] == "D":
                            can_arrive = True
                            break
    print(can_arrive)
    answer = 0
    return answer