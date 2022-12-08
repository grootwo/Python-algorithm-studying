# 1992
# 쿼드트리
import sys

n = int(input())
graph = list(sys.stdin.readline().rstrip() for _ in range(n))


def print_or_cut(x, y, n):
    num = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != graph[i][j]:
                print('(', end='')
                print(print_or_cut(x, y, n//2), end='')
                print(print_or_cut(x, y+n//2, n//2), end='')
                print(print_or_cut(x+n//2, y, n//2), end='')
                print(print_or_cut(x+n//2, y+n//2, n//2), end='')
                print(')', end='')
                return ''
    return num


print(print_or_cut(0, 0, n), end='')