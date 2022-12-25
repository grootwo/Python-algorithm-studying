# 10830
# 행렬 제곱
import sys

n, power = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

mat_temp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        mat_temp[i][j] = mat[i][j]
mat_result = [[0] * n for _ in range(n)]

for l in range(power - 1):
    # 곱셈 한 번 실행
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mat_result[i][j] += mat_temp[i][k] * mat[k][j]
    print(l, '-----------')
    for i in range(n):
        print(*mat_result[i])
    # temp에 result값 옮겨주기
    for i in range(n):
        for j in range(n):
            mat_temp[i][j] = mat_result[i][j]
    for i in range(n):
        print(*mat_temp[i])

for i in range(n):
    print(*mat_result[i])