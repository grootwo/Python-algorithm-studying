# 2587
# 대표값2
import sys

case = 5
nums_list = []
for i in range(case):
    nums_list.append(int(sys.stdin.readline()))
nums_list.sort()

sum = 0
for i in nums_list:
    sum += i
avg = int(sum / case)
mid = nums_list[2]

print(avg)
print(mid)