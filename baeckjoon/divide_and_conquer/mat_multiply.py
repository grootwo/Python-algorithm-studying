# 2740
# 행렬곱셈
import sys

row_a, col_a = map(int, input().split())
mat_a = [list(map(int, sys.stdin.readline().split())) for _ in range(row_a)]

row_b, col_b = map(int, input().split())
mat_b = [list(map(int, sys.stdin.readline().split())) for _ in range(row_b)]

# 곱셈 행렬 초기화
new_mat = [[0 for _ in range(len(mat_b[0]))] for _ in range(len(mat_a))]

for i in range(len(mat_a)):
    for j in range(len(mat_b[0])):
        for k in range(len(mat_b)):
            new_mat[i][j] += mat_a[i][k] * mat_b[k][j]

for i in range(len(new_mat)):
    print(*new_mat[i])