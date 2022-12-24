# 18870
# 좌표 압축
import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

nums_sort = sorted(list(set(nums)))
dic = {}
for i in range(len(nums_sort)):
    dic[nums_sort[i]] = i

for i in range(n):
    print(dic[nums[i]], end=' ')