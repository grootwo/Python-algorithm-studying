# 1012
# 유기농 배추

import sys
sys.setrecursionlimit(10**6)

# 케이스 입력받기
case_num = int(input())
worm_count = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(graph, y, x, row, col):
    if (x < 0 or x >= row) or (y < 0 or y >= col):
        return False
    if graph[y][x] == 1:
        # 방문 표시
        graph[y][x] = 0
        # 방문 배추의 동서남북 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(graph, ny, nx, row, col)
        return True
    else:
        return False


for i in range(case_num):
    # 배추밭의 가로, 세로 길이, 배추 개수 입력받기
    row, col, count = map(int, sys.stdin.readline().split())

    # 배열로 배추 전개도 그리기
    graph = [[0] * row for _ in range(col)]
    for _ in range(count):
        c, r = map(int, sys.stdin.readline().split())
        # 배추 위치 표시
        graph[r][c] = 1

    # 동서남북 붙어 있는 배추 파악하기
    for j in range(col):
        for k in range(row):
            if graph[j][k] == 1:
                if dfs(graph, j, k, row, col) == True:
                    worm_count += 1

    print(worm_count)
    worm_count = 0
