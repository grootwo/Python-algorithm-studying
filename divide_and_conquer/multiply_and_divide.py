# 1629
# 곱셈
import sys

num, multiplier,divider = map(int, sys.stdin.readline().split())

result = (num ** multiplier) % divider

print(result)