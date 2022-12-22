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
    max_count = nums.count(nums[0])
    max_num = [nums[0]]
    for i in range(1, len(nums)):
        count = nums.count(nums[i])
        if max_count < count:
            max_count = count
            # 초기화
            max_num = [nums[i]]
        elif max_count == count:
            if nums[i] not in max_num:
                max_num.append(nums[i])
        else:
            continue
    max_num.sort()
    if len(max_num) != 1:
        return max_num[1]
    else:
        return max_num[0]


def get_scope(nums):
    return nums[-1] - nums[0]


print(get_mean(nums))
print(get_median(nums))
print(get_mode(nums))
print(get_scope(nums))