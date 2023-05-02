# Lv.1
# 덧칠하기
def solution(n, m, section):
    from collections import deque
    que = deque(section)
    result = 0
    while que:
        min_s = que[0]
        for i in range(m):
            if que and que[0] < min_s + m:
                que.popleft()
        result += 1
        #print(que)
    answer = result
    return answer
