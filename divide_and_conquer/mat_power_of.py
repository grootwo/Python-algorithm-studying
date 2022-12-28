# 10830
# 행렬 제곱
# ref(https://junior-datalist.tistory.com/223)
import sys

n, power = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 행렬 곱셈
def mat_multiply(mat_a, mat_b):
    mat_result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mat_result[i][j] += mat_a[i][k] * mat_b[k][j]
            mat_result[i][j] %= 1000
    return mat_result


def divdie_power(mat, power):
    if power == 1:
        # 여기에 바로 1000 나눈 나머지 넣어도 되는지 고민
        return mat
    elif power % 2 == 0:
        temp = divdie_power(mat, power//2)
        return mat_multiply(temp, temp)
    elif power % 2 == 1:
        temp = divdie_power(mat, n - 1)
        return mat_multiply(temp, temp)

result = divdie_power(mat, power)

for i in range(n):
    print(*result[i])