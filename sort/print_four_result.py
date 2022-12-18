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
    check = []
    i = 0
    while i < len(nums):
        num = nums[i]
        count = nums.count(num)
        check.append([num, count]) # 수와 해당 수의 개수를 저장
        i += count # 셈이 중복되지 않도록
    check.sort(key=lambda x:(-x[1], x[0]))
    if len(check) >= 2 and check[0][1] == check[1][1]: # 만약 원소가 2개 이상이고, 빈도수가 같은 원소가 있다면
        return check[1][0] # 두 번째로 작은 수를 리턴
    else:
        return check[0][0]


def get_scope(nums):
    return nums[-1] - nums[0]


print(get_mean(nums))
print(get_median(nums))
print(get_mode(nums))
print(get_scope(nums))