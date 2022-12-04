# 1780
# 색종이의 개수
import sys


def check_num(graph):
    num = graph[0][0]
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] != num:
                return False


n = int(input())
graph = []
for i in range(n):
    graph.append(map(int, sys.stdin.readline().split()))
print(graph)