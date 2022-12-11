# 1629
# 곱셈
import sys
from collections import deque
from math import floor

num, power_num, divider = map(int, sys.stdin.readline().split())
que = deque([num for _ in range(power_num)])


while len(que) != 1:
    for i in range(floor(len(que) / 2)):
        que[i] *= que.pop()

print(que.popleft() % divider)