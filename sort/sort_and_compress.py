# 18870
# 좌표 압축
import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

nums_sort = []
for i in range(n):
    if nums[i] not in nums_sort:
        nums_sort.append(nums[i])
nums_sort.sort()

for i in range(n):
    index = nums_sort.index(nums[i])
    print(index, end=' ')