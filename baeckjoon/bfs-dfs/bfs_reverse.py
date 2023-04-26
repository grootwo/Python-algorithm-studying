# 24445
# bfs

import sys
from collections import deque   # 양방향 큐

# 정점 수, 간선 수, 시작 정점 입력받기
n, m, r = map(int, sys.stdin.readline().split())

# 그래프
graph = [[] for _ in range(n + 1)]

# 방문 여부
visited = [0] * (n + 1)

# bfs
def bfs(graph, r, visited):
    queue = deque([r])  # [r]이 뭔가
    visited[r] = 1  # 첫번째 방문 정점
    count = 2  # 두번째 방문 정점
    while queue:
        r = queue.popleft()
        for i in graph[r]:
            if visited[i] == 0:
                queue.append(i)  # add to the end
                visited[i] = count
                count += 1

# 그래프 입력
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 그래프 내림차순으로 정렬
for i in range(n + 1):
    graph[i].sort()
    graph[i].reverse()

bfs(graph, r, visited)

# 순서 출력
for i in range(n + 1):
    if i != 0:
        print(visited[i])