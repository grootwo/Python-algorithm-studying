# 2108
# 통계학
import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()


def get_mean(nums):
    sum = 0
    for i in nums:
        sum += i
    mean = round(sum / len(nums))
    return mean


def get_median(nums):
    return nums[len(nums) // 2]


def get_mode(nums):
    nums_counter = Counter(nums).most_common()
    if len(nums_counter) > 1 and nums_counter[0][1] == nums_counter[1][1]:
        return nums_counter[1][0]
    else:
        return nums_counter[0][0]


def get_scope(nums):
    return nums[-1] - nums[0]


print(get_mean(nums))
print(get_median(nums))
print(get_mode(nums))
print(get_scope(nums))