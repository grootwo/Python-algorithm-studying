# 1260
# dfs와 bfs

import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque

# 정점, 간선, 시작 정점
n, m, r = map(int, sys.stdin.readline().split())

visited_dfs = [0] * (n + 1)
visited_bfs = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    num1, num2 = map(int, sys.stdin.readline().split())
    # 무방향 그래프
    graph[num1].append(num2)
    graph[num2].append(num1)

for i in range(n + 1):
    graph[i].sort()


def dfs(e, r, visited):
    visited[r] = 1
    print(r, end=' ')
    for i in e[r]:
        if visited[i] == 0:
            dfs(e, i, visited)


def bfs(e, r, visited):
    visited[r] = 1
    queue = deque([r])
    # 자신과 연결된 모든 방문 노드를 큐에 쓰고 팝
    while queue:
        r = queue.popleft()
        print(r, end=' ')
        for i in e[r]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)


dfs(graph, r, visited_dfs)
print()
bfs(graph, r, visited_bfs)
