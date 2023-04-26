# 1992
# 쿼드트리
import sys

n = int(input())
graph = list(sys.stdin.readline().rstrip() for _ in range(n))


def print_or_cut(x, y, n):
    num = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 이차원 리스트 안의 원소가 하나라도 다르다면
            if num != graph[i][j]:
                # 괄호 출력, 이차원 리스트 쪼개기
                print('(', end='')
                print(print_or_cut(x, y, n//2), end='')
                print(print_or_cut(x, y+n//2, n//2), end='')
                print(print_or_cut(x+n//2, y, n//2), end='')
                print(print_or_cut(x+n//2, y+n//2, n//2), end='')
                print(')', end='')
                return ''
    # 이차원 리스트 안의 원소가 모두 같다면 해당 원소 출력
    return num


print(print_or_cut(0, 0, n), end='')