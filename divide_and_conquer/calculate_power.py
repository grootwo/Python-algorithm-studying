# 1629
# 곱셈
import sys
from collections import deque

num, power_num, divider = map(int, sys.stdin.readline().split())
que = deque([num for _ in range(power_num)])

while len(que) != 1:
    num = que.pop()
    num = que.pop() * num
    que.appendleft(num)
    print(que)

print(que.popleft() % divider)