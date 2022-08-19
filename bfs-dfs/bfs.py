# 24444
# bfs
# 참고(https://anggeum.tistory.com/m/entry/24444-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%88%98%EC%97%85-%EB%84%88%EB%B9%84-%EC%9A%B0%EC%84%A0-%ED%83%90%EC%83%89-1-%EC%A0%95%EC%A0%90-%EB%B0%A9%EB%AC%B8-%EC%88%9C%EC%84%9C-%EA%B5%AC%ED%98%84)
# deque 참고(https://leonkong.cc/posts/python-deque.html)

import sys
from collections import deque

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

# 그래프 오름차순으로 정렬
for i in range(n + 1):
    graph[i].sort()

bfs(graph, r, visited)

# 순서 출력
for i in range(n + 1):
    if i != 0:
        print(visited[i])

# 반복문으로 시도
# def bfs(graph, v, visited):
#     global count
#     visited[v] = count
#     for i in graph[v]:
#         if visited[i] == 0:
#             count += 1
#             visited[i] = count