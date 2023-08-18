def solution(n):
    nums = list(int(cha) for cha in str(n))
    nums.sort()
    nums.reverse()
    return ''.join(nums)
