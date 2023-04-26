# 16928
# 뱀과 사다리 게임
from collections import deque

ladder_count, snake_count = map(int, input().split())

# 전개도 그리기(1부터 시작)
graph = [0] * (101)

# 사다리, 뱀(이동 조건) 저장
map_dic = {}
for i in range(ladder_count + snake_count):
    num1, num2 = map(int, input().split())
    map_dic[num1] = num2


def bfs_ladder_game():
    queue = deque()
    queue.append(1)
    while queue:
        now = queue.popleft()
        # 주사위를 굴려 나올 수 있는 결과 모두 실행
        for i in range(1, 7):
            next = now + i
            # 만약 다음 좌표가 인덱스 범위를 충족한다면
            if 0 <= next < 101:
                # 만약 사다리나 뱀이 존재한다면
                if next in map_dic:
                    next = map_dic.get(next)
                # 처음 방문한다면
                if graph[next] == 0:
                    graph[next] = graph[now] + 1
                    queue.append(next)
                # 다시 방문한다면
                elif graph[next] > graph[now] + 1:
                    graph[next] = graph[now] + 1
                    queue.append(next)
    return graph[100]

print(bfs_ladder_game())
