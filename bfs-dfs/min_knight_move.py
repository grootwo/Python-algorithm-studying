# 7562
# 나이트의 이동
from collections import deque

test_case = int(input())

kx = [1, 1, -1, -1, 2, 2, -2, -2] # knight의 x 이동 범위
ky = [2, -2, 2, -2, 1, -1, 1, -1] # knight의 y 이동 범위

# square를 어디에 정의하지?

def bfs(x1, y1, x2, y2, square):
    queue = deque()
    queue.append((x1, y1))
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + kx[i]
            ny = y + ky[i]
            # 만약 인덱스를 벗어난다면
            if nx < 0 or nx >= square or ny < 0 or ny >= square:
                continue
            else:
                # 만약 처음 방문한다면
                if graph[nx][ny] == None:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
                # 만약 길이라면
                else:
                    if graph[nx][ny] < graph[x][y] + 1:
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append((nx, ny))
                    else:
                        continue
    return graph[x2][y2]


for i in range(test_case):
    square = int(input())
    # 체스판 만들기
    graph = [[None] * square for i in range(square)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    graph[start_x][start_y] = 0
    print(bfs(start_x, start_y, end_x, end_y, square))
