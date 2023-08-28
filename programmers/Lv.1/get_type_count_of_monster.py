# Lv.1
# 폰켓몬
from collections import Counter
def solution(nums):
    count = list(Counter(nums).values())
    if len(count) >= len(nums) // 2: # 폰켓몬의 종류가 데려갈 수 있는 수 이상일 경우
        return len(nums) // 2
    else:
        return len(count) # 폰켓몬의 종류가 데려살 수 있는 수 미만일 경우
