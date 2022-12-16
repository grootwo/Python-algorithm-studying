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
    mean = round(sum / len(nums))
    return mean


def get_median(nums):
    return nums[round(len(nums) / 2)]


def get_mode(nums):
    max_count = 0
    check = []
    for i in range(len(nums)):
        if nums[i] not in check and nums.count(i) >= max_count:
            max_count = nums.count(i)
            check.append(nums[i])
        else:
            continue



def get_scope(nums):
    return nums[-1] - nums[0]


print(get_mean(nums))
print(get_median(nums))
# print(get_mode())
print(get_scope(nums))