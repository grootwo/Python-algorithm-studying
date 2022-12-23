# 18870
# 좌표 압축
import sys
from collections import Counter

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

nums_counter = Counter(nums)
print(nums_counter)
nums_sort = [0] * len(nums_counter)
print(nums_counter)
for i in range(len(nums_counter)):
    index = nums.index(nums_counter[i][0])
    print('i', index)
    nums_sort[index] = nums_counter[i][1]
    print(nums_sort)
    print('------')

for i in range(n):
    index = nums_sort.index(nums[i])
    if i != len(nums) - 1:
        print(index, end=' ')
    else:
        print(index)