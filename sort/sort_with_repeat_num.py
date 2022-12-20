# 10989
# 수 정렬하기 3
# 참고(https://pacific-ocean.tistory.com/67)
import sys

n = int(sys.stdin.readline())

nums = [0] * 10001

for _ in range(n):
    nums[int(sys.stdin.readline())] += 1

for i in range(10001):
    if nums[i] != 0:
        for _ in range(nums[i]):
            print(i)