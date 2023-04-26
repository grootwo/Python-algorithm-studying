# 10807
# 개수 세기

case = int(input())
nums = list(map(int, input().split()))
num = int(input())

count = 0
for i in range(case):
    if nums[i] == num:
        count += 1

print(count)