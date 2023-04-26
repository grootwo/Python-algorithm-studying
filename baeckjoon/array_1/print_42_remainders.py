# 3052
# 나머지

nums = []
for i in range(10):
    nums.append(int(input()))

remainders = []
for i in range(10):
    remainder = nums[i] % 42
    if remainder not in remainders:
        remainders.append(remainder)

print(len(remainders))