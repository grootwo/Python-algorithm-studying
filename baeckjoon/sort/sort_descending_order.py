# 1427
# 소트인사이트

nums_str = input()
nums = []

for i in nums_str:
    nums.append(int(i))

nums.sort()
nums.reverse()

for i in nums:
    print(i, end='')