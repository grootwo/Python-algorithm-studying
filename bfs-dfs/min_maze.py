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



