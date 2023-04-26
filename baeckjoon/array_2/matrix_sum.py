# 2738
# 행렬 덧셈

row, col = map(int, input().split())

matrix = []

for i in range(row * 2):
    matrix.append(list(map(int, input().split())))

for i in range(row):
    for j in range(col):
        print("{} ".format(matrix[i][j] + matrix[i + row][j]), end="")
    print()