# 2206
# 벽 부수고 이동하기
from collections import deque

row, col = map(int, input().split())
graph = []

# 미로 전개도 입력받고 그리기
for i in range(row):
    graph.append(list(map(int, input())))

# 방문 표시 배열 3차원 배열 visited[행][열][부수기 여부]
visited = [[[0] * 2 for _ in range(col)] for _ in range(row)]
# 시작점 초기화
visited[0][0][0] = 1

# 동서남북 확인 좌표
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]


def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))
    while queue:
        x, y, z = queue.popleft()
        if x == row - 1 and y == col - 1:
            return visited[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 만약 인덱스를 벗어난다면
            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue
            # 만약 길이 아니고, 벽을 부수지 않았다면
            if graph[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))
            # 만약 길이라면
            if graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
    return -1


print(bfs(0, 0, 0))