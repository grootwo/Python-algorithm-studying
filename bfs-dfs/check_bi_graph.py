# 1707
# 이분 그래프
from collections import deque

test_case = int(input())


def bfs(x, index):
    while queue:
        x, index = queue.popleft()
        visited[x] = True
        # 기록할 이분 그래프 인덱스
        if index == 0:
            index_next = 1
        else:
            index_next = 0
        for j in graph[x]:
            if visited[j] == False:
                graph_bi[index_next].append(j)
                queue.append((j, index_next))


def check_bi_graph():
    for j in graph_bi[0]:
        if j in graph_bi[1]:
            return False
    # 만약 그래프가 이어져 있지 않아서 방문되지 않았다
    for j in range(1, len(visited) + 1):
        if visited[j] is False:
            return False
    return True


for i in range(test_case):
    ver, edge = map(int, input().split())
    # 간선 정보 나타낼 그래프
    graph = [[] for _ in range(ver + 1)]
    # 방문 여부 표시 배열
    visited = [False] * (ver + 1)
    # 데이터 입력받아 그래프로 기록
    for j in range(edge):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    # 그래프 오름차순으로 정렬
    for j in range(1, ver + 1):
        graph[j].sort()
    # 이분 그래프 확인할 그래프 집합
    graph_bi = [[] for _ in range(2)]
    graph_bi[0].append(1)
    queue = deque()
    queue.append((1, 0))
    bfs(1, 0)
    # 이분 그래프인지 확인
    if check_bi_graph() is True:
        print("YES")
    else:
        print("NO")