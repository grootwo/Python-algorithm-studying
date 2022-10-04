# 1697
# 숨바꼭질
from collections import deque

start, end = map(int, input().split())

if end > start:
    index = end * 2
else:
    index = start * 2

graph = [None] * (index + 1)
graph[start] = 0


def bfs(now, end):
    queue = deque()
    queue.append(now)
    while queue:
        now = queue.popleft()
        for i in range(3):
            if i == 0:
                next = now * 2
            elif i == 1:
                next = now + 1
            else:
                next = now - 1
            # 만약 인덱스를 벗어난다면
            if next > end * 2 or next < 0:
                continue
            # 만약 처음 방문한다면
            if graph[next] == None:
                graph[next] = graph[now] + 1
                queue.append(next)
            # 이미 방문했던 곳이라면
            else:
                # 최소의 값을 입력
                if graph[next] > (graph[now] + 1):
                    graph[next] = graph[now] + 1
                    queue.append(next)
    return graph[end]


print(bfs(start, end))