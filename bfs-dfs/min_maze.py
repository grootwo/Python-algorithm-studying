# 2178
# 미로 탐색
import sys
sys.setrecursionlimit(10**6)

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

# 그러면 모두 다 세지 않고 목적지에 도착했다면 그 경로까지의 길의 개수를 기록하고 비교하는 방법이 필요하다
# 이게 여러 그룹을 세는 것이 아니니까 False를 리턴하면 안되고, 배열의 좌표를 벗어나면 다음으로 돌아가야 함

# 1. dfs로 시작점에서 목적지로 향한다
# 2. 목적지에 닿을 때 최소의 노드 개수를 출력한다

# 그러면 return문을 이용하되, 뭘 하면 될까?
# 생각 1: 목적지에 닿아도 1을 0으로 바꿔주지 않고 여러 경우에 닿은 count 중 min을 출력하면 되나?
# 생각 2: 깊이를 세면 되는데!!!!

def dfs(x, y):
    # 만약 그래프 밖을 벗어난다면
    if x < 0 or x >= row or y < 0 or y >= col:
        return

    global count

    # 만약 길이라면
    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        # 만약 목적지에 도달했다면
        if x == (row - 1) and y == (col - 1):
            print("middle count: ", count)
            return count
        else:
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                dfs(next_x, next_y)
    else:
        return


print(dfs(0, 0), count)

for i in range(row):
    print(graph[i])
