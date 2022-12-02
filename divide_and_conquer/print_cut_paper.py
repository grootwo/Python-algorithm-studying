# 2630
# 색종이 만들기
import sys
from collections import deque

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
count = 0
que = deque([])
que.append(graph)
while que:
    check_list = que.popleft()
    if check_same(que) is True:
        count += 1
    else:
        length = len(check_list)
        if length != 1:
            for i in range(4):
                # 2사분면
                temp_list1 = check_list[0:length/2]
                for j in range(length/2):
                    temp_list1[j][0:length/2]
                # 3사분면
                temp_list2 = check_list[length/2:length]
                for j in range(length/2):
                    temp_list2[j][0:length/2]
                # 1사분면
                temp_list3 = check_list[0:length/2]
                for j in range(length/2):
                    temp_list2[j][length/2:length]
                # 4사분면
                temp_list3 = check_list[length/2:length]
                for j in range(length/2):
                    temp_list2[j][length/2:length]
