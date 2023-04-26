# 2667
# 단지번호붙이기
# 참고(https://velog.io/@falling_star3/%EB%B0%B1%EC%A4%80Python-2667%EB%B2%88-%EB%8B%A8%EC%A7%80%EB%B2%88%ED%98%B8%EB%B6%99%EC%9D%B4%EA%B8%B0)

import sys
sys.setrecursionlimit(10**6)

n = int(input())

graph = [[] for _ in range(n)]
num = []
count = 0
group_count = 0

# 동서남북 확인
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph[i] = list(sys.stdin.readline())
    # 줄바꿈 문자 삭제
    graph[i].remove('\n')

# 그래프 정수로 처리
for i in range(n):
    for j in range(n):
        graph[i][j] = int(graph[i][j])


def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        # 카운트 후 방문 표시
        graph[x][y] = 0
        # 동서남북 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False


for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            num.append(count)
            group_count += 1
            count = 0

num.sort()
print(group_count)
for i in range(len(num)):
    print(num[i])