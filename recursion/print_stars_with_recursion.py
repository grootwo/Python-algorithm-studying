# 2447
# 별 찍기 - 10

n = int(input())
graph = [[' '] * n for _ in range(n)]


def divide_and_get_star(row, col, length):
    if length == 1:
        graph[row][col] = '*'
        return
    next_length = length // 3
    divide_and_get_star(row, col, next_length)
    divide_and_get_star(row, col + next_length, next_length)
    divide_and_get_star(row, col + next_length * 2, next_length)
    divide_and_get_star(row + next_length, col, next_length)
    divide_and_get_star(row + next_length, col + next_length * 2, next_length)
    divide_and_get_star(row + next_length * 2, col, next_length)
    divide_and_get_star(row + next_length * 2, col + next_length, next_length)
    divide_and_get_star(row + next_length * 2, col + next_length * 2, next_length)
    return


divide_and_get_star(0, 0, n)
for i in range(n):
    for j in range(n):
        print(graph[i][j], end="")
    print()