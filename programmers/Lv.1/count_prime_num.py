def solution(n):
    nums = [i for i in range(1, n + 1)]
    count = 0
    for num in nums:
        for i in range(2, int(n ** 0.5) + 1):
            if i >= num:
                break
            if num % i == 0:
                count += 1
                break
    return len(nums) - count - 1 # 1 제외
