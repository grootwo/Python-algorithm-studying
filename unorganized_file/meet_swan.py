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


# 지나간 길은 표시해야 한다
# 백조가 모두 L로 표시된다
def can_meet(swan_r, swan_c):
    visited = [[0] * col for _ in range(row)]
    visited[swan_r][swan_c] = 1
    print(visited)
    que = deque()
    que.append([swan_r, swan_c])
    while que:
        r, c = que.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nr < row and 0 <= nc < col and visited[nr][nc] == 0:
                for j in range(len(visited)):
                    print(*visited[j])
                print("-----")
                if lake_graph[nr][nc] == ".":
                    que.append([nr, nc])
                    visited[nr][nc] = 1
                elif lake_graph[nr][nc] == "L":
                    return True
    return False


count_day = 0
