# 1966
# 프린터 큐
import sys
from collections import deque

case = int(input())


def check_max_importance(lists):
    max_importance = 1
    for j in lists:
        if max_importance < j[1]:
            max_importance = j[1]
    # 현재 리스트 중 가장 높은 중요도를 리턴
    return max_importance


def print_count(queue):
    count = 0
    while queue:
        # 중요도가 가장 높다면 세기
        if queue[0][1] == check_max_importance(queue):
            count += 1
            temp = queue.popleft()
            # 만약 궁금했던 문서라면 count 출력
            if temp[0] == curious_num:
                print(count)
                return
        # 중요도가 낮다면 뒤로 보내기
        else:
            temp = queue.popleft()
            queue.append(temp)


for i in range(case):
    document_count, curious_num = map(int, input().split())
    queue = deque([])
    importances = list(map(int, input().split()))
    # 문서와 중요도 queue에 저장
    for j in range(document_count):
        queue.append([j, importances[j]])
    print_count(queue)