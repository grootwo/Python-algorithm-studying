# 2562
# 최댓값

nums = []

for i in range(9):
    nums.append(int(input()))

max_num = max(nums)
max_num_index = nums.index(max_num) + 1

print(max_num)
print(max_num_index)