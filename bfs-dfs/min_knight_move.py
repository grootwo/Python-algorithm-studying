# 7562
# 나이트의 이동
from collections import deque

test_case = int(input())

kx = [1, 1, -1, -1, 2, 2, -2, -2] # knight의 x 이동 범위
ky = [2, -2, 2, -2, 1, -1, 1, -1] # knight의 y 이동 범위

def bfs(x1, y1, x2, y2, square):
    queue = deque()
    queue.append((x1, y1))
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + kx[i]
            ny = y + ky[i]
            # 체스판 안이고, 방문하지 않았다면
            if 0 <= nx < square and 0 <= ny < square and graph[nx][ny] == None:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
            if graph[x2][y2] != None:
                return graph[x2][y2]


for i in range(test_case):
    square = int(input())
    # 체스판 만들기
    graph = [[None] * square for i in range(square)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    graph[start_x][start_y] = 0
    print(bfs(start_x, start_y, end_x, end_y, square))
