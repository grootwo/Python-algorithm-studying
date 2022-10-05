# 7576
# 토마토

row, col = map(int, input().split())
graph = []

for i in range(col):
    graph.append(list(map(int, input().split())))

for i in range(col):
    print(graph[i])