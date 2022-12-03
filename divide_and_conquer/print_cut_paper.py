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
            if check_num != i:
                return -1
    if check_num == 0:
        return 0
    elif check_num == 1:
        return 1


# que에 리스트를 넣는다
# 그 리스트를 확인한다
# 만약 모두 같지 않다면 분할하여 큐에 넣는다
# 만약 리스트의 원소가 하나라면 최소이니 더 이상 분할하지 않는다
count_0 = 0
count_1 = 0
que = deque([])
que.append(graph)
while que:
    check_list = que.popleft()
    print('---------')
    print(check_list)
    length = len(check_list)
    print('len', length)
    if length == 1: # 만약 원소가 최소라면
        if check_list.pop() == 0:
            count_0 += 1
            print('0++')
        else:
            count_1 += 1
            print('1++')
    else: # 만약 2차원 리스트라면
        check = check_same(check_list)
        print('check', check)
        if check == 0:
            count_0 += 1
            print('0++')
        elif check == 1:
            count_1 += 1
            print('1++')
        else:
            if length != 1:
                next_length = int(length / 2)
                temp_list1 = check_list[0:next_length]
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
                print('1', temp_list1)
                print('2', temp_list2)
                print('3', temp_list3)
                print('4', temp_list4)

print(count_0)
print(count_1)