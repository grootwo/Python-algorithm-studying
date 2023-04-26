# 2178
# 미로 탐색
# 참고(https://bmy1320.tistory.com/entry/%EB%B0%B1%EC%A4%80-Silver-1%EB%AC%B8%EC%A0%9C-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-2178-%EB%AF%B8%EB%A1%9C-%ED%83%90%EC%83%89)

import sys
from collections import deque

# 가로, 세로 입력받기
row, col = map(int, sys.stdin.readline().split())
graph = []

# 미로 전개도 입력받고 그리기
for i in range(row):
    graph.append(list(map(int, input())))

# 동서남북 확인 좌표
# 남, 동쪽으로 먼저 확인
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 만약 인덱스를 벗어난다면
            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue
            # 만약 길이 아니라면
            if graph[nx][ny] == 0:
                continue
            # 만약 길이라면
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[row - 1][col - 1]

print(bfs(0, 0))