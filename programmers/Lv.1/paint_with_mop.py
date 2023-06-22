# Lv.1
# 덧칠하기
def solution(n, m, section):
    from collections import deque
    que = deque(section)
    result = 0
    while que:
        min_s = que[0]
        # 페인트 한 번 최대로 칠하고, 칠한 부분 삭제하기
        for i in range(m):
            if que and que[0] < min_s + m:
                que.popleft()
        result += 1
    answer = result
    return answer
