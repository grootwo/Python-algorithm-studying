# 16928
# 뱀과 사다리 게임
from collections import deque

ladder_count, snake_count = map(int, input().split())

# 전개도 그리기
graph = [0] * (100)

# 사다리, 뱀(이동 조건) 저장
map_dic = {}
for i in range(ladder_count + snake_count):
    num1, num2 = map(int, input().split())
    map_dic[num1] = num2


def bfs_ladder_game():
    queue = deque()
    deque.append(0)
    while queue:
        now = queue.popleft()
        for i in range(1, 7):
            next = now + i
            # 만약 다음 좌표가 인덱스 범위를 충족한다면
            if 0 <= next < 100:
                # 만약 사다리나 뱀이 존재한다면