# 1780
# 색종이의 개수
import sys

n = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

count = [0, 0, 0]


def count_or_cut_paper(x, y, n):
    global count_minus_1, count_0, count_1
    num = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != graph[i][j]:
                count_or_cut_paper(x, y, n//3)
                count_or_cut_paper(x, y+n//3, n//3)
                count_or_cut_paper(x, y+n//3*2, n//3)
                count_or_cut_paper(x+n//3, y, n//3)
                count_or_cut_paper(x+n//3, y+n//3, n//3)
                count_or_cut_paper(x+n//3, y+n//3*2, n//3)
                count_or_cut_paper(x+n//3*2, y, n//3)
                count_or_cut_paper(x+n//3*2, y+n//3, n//3)
                count_or_cut_paper(x+n//3*2, y+n//3*2, n//3)
                return
    count[num] += 1


count_or_cut_paper(0, 0, n)
print(count[-1])
print(count[0])
print(count[1])