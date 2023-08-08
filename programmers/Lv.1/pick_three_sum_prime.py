from itertools import combinations
def solution(nums):
    nums = sorted(set(sum(i) for i in list(combinations(nums, 3))))
    print(nums)
    count = 0
    return count
