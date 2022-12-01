# 2630
# 색종이 만들기
import sys

n = int(input())

# 데이터를 입력받아 그래프로 표현
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


def check_same(graph):
    check_num = graph[0][0]
    for i in range(len(graph) * len(graph[0])):
        if check_num != i:
            return False
    return True


graph1 = graph[0:2][0:2]
print(graph1)
print(check_same(graph1))