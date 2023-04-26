# 4344
# 평균은 넘겠지
import sys

test_case = int(input())

# 평균을 넘는 학생들의 비율들 저장
over_avg_percent = []

for i in range(test_case):
    nums = list(map(int, sys.stdin.readline().split()))
    # 평균 계산
    sum = 0
    for j in range(1, nums[0] + 1):
        sum += nums[j]
    avg = sum / nums[0]
    # 평균 넘는 학생 수 세기
    count = 0
    for j in range(1, nums[0] + 1):
        if nums[j] > avg:
            count += 1
    # 평균을 넘는 학생들의 비율 계산
    std_over_avg = count / nums[0]
    over_avg_percent.append(std_over_avg)
    nums.clear()

for i in over_avg_percent:
    # 퍼센트로 바꾸어 출력
    print("{0:.3f}%".format(i*100))