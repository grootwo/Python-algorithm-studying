from itertools import combinations
def solution(nums):
    nums = sorted(set(sum(i) for i in list(combinations(nums, 3))))
    count = 0
    for num in nums:
        count += is_prime(num)
    return count

def is_prime(num):
    if num == 0 or num == 1:
        return 0
    else:
        for i in range(2, (num//2) + 1):
            if num % i == 0:
                return 0
        return 1
