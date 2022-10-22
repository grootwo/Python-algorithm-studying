# 1707
# 이분 그래프

# 그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.
# 그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

# 입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다.
# 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다. 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다.
# 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다.

# K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.

# 제한
# 2 ≤ K ≤ 5
# 1 ≤ V ≤ 20,000
# 1 ≤ E ≤ 200,000

# 2
# 3 2
# 1 3
# 2 3

# 4 4
# 1 2
# 2 3
# 3 4
# 4 2

# YES
# NO
from collections import deque

test_case = int(input())


for i in range(test_case):
    graph = [[] for _ in range(20000 + 1)]
    ver, edge = map(int, input().split())
    # 간선 정보받아 그래프 기록하기
    for j in range(edge):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    # 그래프 오름차순으로 정렬
    for j in range(1, ver + 1):
        graph[j].sort()
    graph1 = []
    graph2 = []
    queue = deque([1])
    while queue:
        x = queue.popleft()
        # 만약 한 쪽 그래프에 있다면 안 써도 됨 -> visisted
        # 이분 그래프인지 확인할 때 1에 있는 게 2에도 있으면 이분 그래프 아님