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


# que에 리스트를 넣는다
# 그 리스트를 확인한다
# 만약 모두 같지 않다면 분할하여 큐에 넣는다
# 만약 리스트의 원소가 하나라면 최소이니 더 이상 분할하지 않는다

que = deque([])

