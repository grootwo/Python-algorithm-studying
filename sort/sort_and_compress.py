# 18870
# 좌표 압축
import sys
from collections import Counter

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

nums_sort = sorted(list(set(nums)))
dic = {}
for i in range(n):
    dic[nums[i]] = nums_sort.index(nums[i])

for i in range(n):
    print(dic[nums[i]], end=' ')