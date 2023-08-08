from itertools import combinations
def solution(nums):
    nums = sorted(set(sum(i) for i in list(combinations(nums, 3))))
    print(nums)
    count = 0
    for i in range(1, max(nums)):
        for j in range(len(nums)):
            if nums[j] % i == 0:
                nums[j] = None
    return len(nums)
