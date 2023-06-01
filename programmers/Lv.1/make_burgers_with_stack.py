# Lv.1
# 햄버거 만들기
from collections import deque
def solution(ingredient):
    que = deque([])
    count = 0
    for ing in ingredient:
        que.append(ing)
        if que[-1] == 1 and len(que) >= 4:
            if que[-4] == 1 and que[-3] == 2 and que[-2] == 3:
                for i in range(4):
                    que.pop()
                count += 1
    answer = count
    return answer
