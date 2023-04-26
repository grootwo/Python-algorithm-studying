# 2164
# 카드2
import sys
from collections import deque

case = int(input())

queue = deque([])

for i in range(1, case + 1):
    queue.append(i)

while len(queue) != 1:
    queue.popleft()
    num = queue.popleft()
    queue.append(num)

print(queue.popleft())