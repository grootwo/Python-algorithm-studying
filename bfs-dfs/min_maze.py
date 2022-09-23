# 2178
# 미로 탐색
import sys

# 가로, 세로 입력받기
row, col = map(int, sys.stdin.readline().split())

graph = [[0] for i in range(row)]

# 미로 전개도 입력받고 그리기
for i in range(row):
    graph[i] = list(sys.stdin.readline())
    # 줄바꿈 문자 삭제
    graph[i].remove('\n')

# 그래프 정수로 처리
for i in range(row):
    for j in range(col):
        graph[i][j] = int(graph[i][j])

for i in range(row):
    print(graph[i])

# 밑, 그리고 오른쪽을 우선시하며 진행해야 함
# 이제껏 해온 방향처럼 갈 수 있는 모든 길을 세면 안됨
# 그러면 일단 가로 막혔는데 목적지가 아니라면 막다른 길이니 카운트를 줄여야 함
# 근데 이것까진 알고리즘이 알아서 할 수 있지 않나
# 그러면 모두 다 세지 않고 목적지에 도착했다면 그 경로까지의 길으 개수를 기록하고 비교하는 방법이 필요하다


