# 1629
# 곱셈
import sys
from collections import deque
from math import floor

num, power_num, divider = map(int, sys.stdin.readline().split())
que = deque([num for _ in range(power_num)])


def power(a, b):
    if b == 1:
        return a
    if b % 2 == 0:
        return power(a, b//2) ** 2
    else:
        return (power(a, b//2) ** 2) * a


print(power(num, power_num) % divider)