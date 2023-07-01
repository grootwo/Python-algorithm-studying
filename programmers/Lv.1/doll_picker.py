from collections import deque
def solution(board, moves):
    stack = deque([])
    count = 0
    for move in moves:
        doll = get_top_doll(move, board)
        if len(stack) > 1 and stack[-1] == doll:
            stack.pop()
            count += 1
        else:
            stack.append(doll)
    return count

def get_top_doll(col, board):
    for i in range(len(board)):
        if board[i][col] != 0:
            return board[i][col]
    return 0
