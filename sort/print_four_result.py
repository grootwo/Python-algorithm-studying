# 2108
# 통계학
import sys

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()


def get_mean(nums):
    sum = 0
    for i in nums:
        sum += i
    mean = int(sum / len(nums))
    return mean


def get_median(nums):
    return nums[len(nums) / 2 + 1]


def get_mode(nums):
    count = 0
    check = []
    # for i in range(len(nums)):
    #     if nums.count()


def get_scope(nums):
    return nums[-1] - nums[0]


print(get_mean(nums))