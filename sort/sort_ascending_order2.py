# 2751
# 수 정렬하기 2
import sys

count = int(sys.stdin.readline())

nums = [int(sys.stdin.readline()) for _ in range(count)]
nums.sort()

for i in nums:
    print(i)