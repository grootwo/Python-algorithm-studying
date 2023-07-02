# Lv.1
# 크레인 인형뽑기 게임
from collections import deque
def solution(board, moves):
    stack = deque([])
    count = 0
    for move in moves:
        doll = get_top_doll(move, board)
        if doll == 0: # 만약 인형이 없다면
            continue
        stack.append(doll)
        while len(stack) > 1 and stack[-2] == stack[-1]: # 두 개 연속으로 같은 인형일 때
            stack.pop()
            stack.pop()
            count += 2
    return count

def get_top_doll(col, board):
    for i in range(len(board)):
        if board[i][col - 1] != 0:
            temp = board[i][col - 1]
            board[i][col - 1] = 0 # 뽑은 인형 제거
            return temp # 뽑은 인형 반환
    return 0
