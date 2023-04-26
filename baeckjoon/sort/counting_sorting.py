# 10989
# 수 정렬하기 3
import sys

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
count_list = [0 for _ in range(max(nums) + 1)]
result_list = [0 for _ in range(n + 1)]
print(result_list)

for i in nums:
    if count_list[i] == 0: # 중복 셈 방지
        count = nums.count(i)
        count_list[i] = count

for i in range(1, len(count_list)):
    count_list[i] += count_list[i - 1]

for i in nums:
    index = count_list[i]
    count_list[i] -= 1
    result_list[index] = i

for i in range(1, n + 1):
    print(result_list[i])