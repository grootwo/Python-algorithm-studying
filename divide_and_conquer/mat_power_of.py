# 10830
# 행렬 제곱
# ref(https://junior-datalist.tistory.com/223)
import sys

n, power = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 행렬 곱셈
def mat_multiply(mat_a, mat_b):
    # print('func mul')
    mat_result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mat_result[i][j] += mat_a[i][k] * mat_b[k][j]
            mat_result[i][j] %= 1000
    # for i in range(n):
    #     print(*mat_result[i])
    return mat_result

# 제곱 분할
def divdie_power(mat, power):
    # print('func pow')
    if power == 1:
        # print('power = 1')
        for i in range(n):
            for j in range(n):
                mat[i][j] %= 1000
        return mat
    elif power % 2 == 0:
        # print('power % 2 == 0')
        # print('power', power)
        temp = divdie_power(mat, power//2)
        return mat_multiply(temp, temp)
    else:
        # print('power % 2 = 1')
        # print('power', power)
        temp = divdie_power(mat, power - 1)
        return mat_multiply(temp, mat)

result = divdie_power(mat, power)

for i in range(n):
    print(*result[i])