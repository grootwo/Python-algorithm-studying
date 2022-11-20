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
    return max_importance


for i in range(case):
    document_count, curious_num = map(int, input().split())
    queue = deque([])
    importances = list(map(int, input().split()))
    for j in range(document_count):
        queue.append([j, importances[j]])
    count = 0
    while queue:
        if queue[0][1] == check_max_importance(queue):
            count += 1
            if queue.popleft() == curious_num:
                break
        else:
            temp = queue.popleft()
            queue.append(temp)
    print(count)


