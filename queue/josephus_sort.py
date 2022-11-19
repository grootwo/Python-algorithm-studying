# 11866
# 요세푸스 문제 0
import sys
from collections import deque

person_count, josephus_num = map(int, input().split())

queue = deque()
for i in range(1, person_count + 1):
    queue.append(i)

print('<', end="")
while len(queue) >= 1:
    for i in range(josephus_num):
        if i != josephus_num:
            queue.append(queue.popleft())
        else:
            print(queue.popleft(), end=", ")
print('>', end="")