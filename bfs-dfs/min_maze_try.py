# 2178
# 미로 탐색
import sys
sys.setrecursionlimit(10**6)

# 가로, 세로 입력받기
row, col = map(int, sys.stdin.readline().split())

map = [[0] for i in range(row)]
total_count = 0

# 동서남북 확인 좌표
# 남, 동쪽으로 먼저 확인
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

# 미로 전개도 입력받고 그리기
for i in range(row):
    map[i] = list(sys.stdin.readline())
    # 줄바꿈 문자 삭제
    map[i].remove('\n')

# 그래프 정수로 처리, 총 1의 개수 세기
for i in range(row):
    for j in range(col):
        map[i][j] = int(map[i][j])
        if map[i][j] == 1:
            total_count += 1

# 전개도를 그래프로 표현하기
graph = [[] for i in range(total_count)]

def dfs(x, y):
    # 만약 그래프 밖을 벗어난다면
    if x < 0 or x >= row or y < 0 or y >= col:
        return

    # 만약 길이라면
    if map[x][y] == 1:
        map[x][y] = 0
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            dfs(next_x, next_y)
    else:
        return

dfs(0, 0)
print(total_count)

for i in range(row):
    print(map[i])
