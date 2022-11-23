# 1021
# 회전하는 큐
import sys
from collections import deque

queue_size, case = map(int, input().split())
index_list = list(map(int, input().split()))

count = 0 # 함수 2, 3 실행 횟수 카운트 변수

# queue에 오름차순으로 수 넣기
queue = deque()
for i in range(1, queue_size + 1):
    queue.append(i)

for i in range(case):
    num = index_list[i]
    while queue[0] != num:
        # 만약 찾으려는 수가 큐의 후반 인덱스에 가깝다면
        if queue.index(num) >= len(queue) / 2:
            queue.rotate(1)
        # 만약 찾으려는 수가 큐의 초반 인덱스에 가깝다면
        else:
            queue.rotate(-1)
        count += 1
    queue.popleft()

print(count)