# Lv.1
# 소수 만들기
from itertools import combinations
def solution(nums):
    count = 0
    for i in combinations(nums, 3):
        count += is_prime(sum(i))
    return count

def is_prime(num):
    if num == 0 or num == 1:
        return 0
    else:
        for i in range(2, (num//2) + 1):
            if num % i == 0:
                return 0
        return 1
