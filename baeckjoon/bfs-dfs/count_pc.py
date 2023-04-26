# 2606
# 바이러스

import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
v = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)
count = 0

for _ in range(v):
    num1, num2 = map(int, sys.stdin.readline().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

for i in range(n + 1):
    graph[i].sort()


def dfs_count(e, r, visited):
    global count
    visited[r] = 1
    count += 1
    for i in e[r]:
        if visited[i] == 0:
            dfs_count(e, i, visited)


dfs_count(graph, 1, visited)
# 총 개수에서 원인 제공 컴퓨터 개수는 -1
print(count - 1)