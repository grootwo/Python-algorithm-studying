def solution(n):
    nums = list(int(cha) for cha in str(n))
    nums.sort()
    nums.reverse()
    answer = list(str(num) for num in nums)
    return int(''.join(answer))
