# 10871
# X보다 작은 수

import sys

count, num = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

for i in range(count):
    if nums[i] < num:
        print(str(nums[i]) + " ", end="")