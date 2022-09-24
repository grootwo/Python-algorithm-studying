# 2178
# 미로 탐색
import sys

# 가로, 세로 입력받기
row, col = map(int, sys.stdin.readline().split())

graph = [[0] for i in range(row)]
count = 0

# 동서남북 확인 좌표
# 남, 동쪽으로 먼저 확인
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

# 미로 전개도 입력받고 그리기
for i in range(row):
    graph[i] = list(sys.stdin.readline())
    # 줄바꿈 문자 삭제
    graph[i].remove('\n')

# 그래프 정수로 처리
for i in range(row):
    for j in range(col):
        graph[i][j] = int(graph[i][j])

# 밑, 그리고 오른쪽을 우선시하며 진행해야 함
# 이제껏 해온 방향처럼 갈 수 있는 모든 길을 세면 안됨
# 그러면 일단 가로 막혔는데 목적지가 아니라면 막다른 길이니 카운트를 줄여야 함
# 근데 이것까진 알고리즘이 알아서 할 수 있지 않나
# 그러면 모두 다 세지 않고 목적지에 도착했다면 그 경로까지의 길으 개수를 기록하고 비교하는 방법이 필요하다
# 이게 여러 그룹을 세는 것이 아니니까 False를 리턴하면 안되고, 배열의 좌표를 벗어나면 다음으로 돌아가야 함

def DFS(x, y):
    if x < 0 or x >= row or y < 0 or y >= col:
        return False

    global count

    if x == (row - 1) and y == (col - 1):
        return count

    if graph[x][y] == 1:
        count += 1
        # 카운트 후 방문 표시
        graph[x][y] = 0
        # 동서남북 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
    return False


if DFS(0, 0):
    print(count)

for i in range(row):
    print(graph[i])
