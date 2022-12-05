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
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if check_num != graph[i][j]:
                return -1
    if check_num == 0:
        return 0
    elif check_num == 1:
        return 1


count_0 = 0
count_1 = 0
que = deque([])
que.append(graph)
while que:
    check_list = que.popleft()
    length = len(check_list)
    if length == 1: # 만약 원소가 최소라면
        num = check_list.pop()
        if num[0] == 0:
            count_0 += 1
        else:
            count_1 += 1
    else: # 만약 2차원 리스트라면
        check = check_same(check_list)
        if check == 0:
            count_0 += 1
        elif check == 1:
            count_1 += 1
        else:
            if length != 1:
                next_length = int(length / 2)
                temp_list1 = check_list[0:next_length]
                # 2사분면
                for j in range(next_length):
                    temp_list1[j] = temp_list1[j][0:next_length]
                que.append(temp_list1)
                # 3사분면
                temp_list2 = check_list[next_length:length]
                for j in range(next_length):
                    temp_list2[j] = temp_list2[j][0:next_length]
                que.append(temp_list2)
                # 1사분면
                temp_list3 = check_list[0:next_length]
                for j in range(next_length):
                    temp_list3[j] = temp_list3[j][next_length:length]
                que.append(temp_list3)
                # 4사분면
                temp_list4 = check_list[next_length:length]
                for j in range(next_length):
                    temp_list4[j] = temp_list4[j][next_length:length]
                que.append(temp_list4)

print(count_0)
print(count_1)