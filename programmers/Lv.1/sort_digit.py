def solution(n):
    nums = sorted(list(str(n)), reverse = True)
    return int(''.join(nums))
