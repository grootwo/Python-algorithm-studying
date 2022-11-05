# 2563
# 색종이

case = int(input())

papers = [list(map(int,input().split())) for _ in range(case)]

# 그래프의 해당 좌표에 색종이가 존재하는 영역 표시하기
graph = [[0] * 100 for _ in range(100)]
for i in range(case):
    x = papers[i][0]
    y = papers[i][1]
    for j in range(x, x + 10):
        for k in range(y, y + 10):
            graph[j][k] = 1

# 그려진 면적 계산하기
count = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1:
            count += 1

print(count)