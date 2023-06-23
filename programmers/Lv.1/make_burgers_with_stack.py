# Lv.1
# 햄버거 만들기
from collections import deque
def solution(ingredient):
    stack = deque([])
    count = 0
    for ing in ingredient:
        stack.append(ing)
        if stack[-1] == 1 and len(stack) >= 4:
            if stack[-4] == 1 and stack[-3] == 2 and stack[-2] == 3:
                for i in range(4):
                    stack.pop()
                count += 1
    answer = count
    return answer
