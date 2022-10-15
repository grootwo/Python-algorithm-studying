# 4344
# 평균은 넘겠지
import sys

test_case = int(input())

over_avg_percent = []
for i in range(test_case):
    nums = list(map(int, sys.stdin.readline().split()))
    print(nums)
    # 평균 계산
    sum = 0
    for j in range(1, nums[0]):
        sum += nums[j]
    avg = sum / nums[0]
    # 평균 넘는 학생 수 세기
    count = 0
    for j in range(1, nums[0]):
        if nums[j] > avg:
            count += 1
    # 평균을 넘는 학생들의 비율 계산
    std_over_avg = count / nums[0]
    over_avg_percent.append(std_over_avg)
    nums.clear()

for i in over_avg_percent:
    print(i)