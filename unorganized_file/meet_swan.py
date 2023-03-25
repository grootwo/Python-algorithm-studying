# 3197
# 백조의 호수
import sys
from collections import deque

row, col = map(int, input().split())

lake_graph = []
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

# 데이터 입력받기
for j in range(row):
    answer = sys.stdin.readline().rstrip()
    lake_graph.append(list(answer))


def melt_ice():
    que = deque()
    for i in range(row):
        for j in range(col):
            if lake_graph[i][j] == ".":
                que.append([i, j])
    while que:
        r, c = que.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nr < row and 0 <= nc < col and lake_graph[nr][nc] == "X":
                lake_graph[nr][nc] = "."


def can_meet(swan_r, swan_c):
    visited = [[0] * col for _ in range(row)]
    visited[swan_r][swan_c] = 1
    que = deque()
    que.append([swan_r, swan_c])
    while que:
        r, c = que.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nr < row and 0 <= nc < col and visited[nr][nc] == 0:
                if lake_graph[nr][nc] == ".":
                    que.append([nr, nc])
                    visited[nr][nc] = 1
                elif lake_graph[nr][nc] == "L":
                    # for j in range(len(visited)):
                    #     print(*visited[j])
                    # print("-----")
                    return True
    # for j in range(len(visited)):
    #     print(*visited[j])
    # print("-----")
    return False


check = False
for r in range(row):
    if check is True:
        break
    for c in range(col):
        if lake_graph[r][c] == "L":
            swan_r = r
            swan_c = c
            check = True
            break

count_day = 0
while can_meet(swan_r, swan_c) is False:
    melt_ice()
    count_day += 1

print(count_day)