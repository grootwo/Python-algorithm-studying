# 10989
# 수 정렬하기 3

n = int(input())
nums = [int(input()) for _ in range(n)]
count_list = [0 for _ in range(max(nums) + 1)]
result_list = [0 for _ in range(n + 1)]

for i in nums:
    count = nums.count(i)
    count_list[i] = count

result = count_list[0] # 누적합
for i in range(1, len(count_list)):
    result += count_list[i]
    count_list[i] = result

for i in nums:
    index = count_list[i]
    count_list[i] -= 1
    result_list[index] = i

for i in range(1, n + 1):
    print(result_list[i])