# 4963
# 섬의 개수

# 다음 자표 이동 범위
dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, 1, -1]

def dfs():
    

width, height = map(int, input().split())

while width != 0 and height != 0:
    graph = [[] for _ in range(height)]
    for i in range(height):
        graph[i] = list(map(int, input().split()))
        print(graph[i])


    width, height = map(int, input().split())
