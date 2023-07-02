from collections import deque
def solution(board, moves):
    stack = deque([])
    count = 0
    for move in moves:
        # print("move:", move)
        doll = get_top_doll(move, board)
        if doll == 0:
            break
        # print("doll:", doll)
        stack.append(doll)
        # print("stack:", stack)
        while len(stack) > 1 and stack[-2] == doll:
            stack.pop()
            stack.pop()
            count += 2
            # print("pop")
            # print("count:", count)
            # print("stack:", stack)
    return count

def get_top_doll(col, board):
    for i in range(len(board)):
        if board[i][col - 1] != 0:
            temp = board[i][col - 1]
            board[i][col - 1] = 0
            return temp
    return 0
