# 2588
# 곱셈

num1 = input()
num2 = input()

nums = []

nums.append(int(num1) * int(num2[2]))
nums.append(int(num1) * int(num2[1]))
nums.append(int(num1) * int(num2[0]))
nums.append(nums[0] + nums[1] * 10 + nums[2] * 100)

for i in nums:
    print(i)