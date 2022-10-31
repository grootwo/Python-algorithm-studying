# 2579
# 계단 오르기
# 참고(https://sungmin-joo.tistory.com/18)

import sys

n = int(input())
stairs = []
max_sum = []
for _ in range(n):
    stairs.append(int(sys.stdin.readline()))

# 인덱스 0부터 시작
max_sum.append(stairs[0])
if n > 1: # OutOfIndex 방지
    max_sum.append(stairs[0] + stairs[1])
if n > 2:
    max_sum.append(max(stairs[0], stairs[1]) + stairs[2])
if n > 3:
    for i in range(3, n):
        max_sum.append(max(stairs[i - 1] + max_sum[i - 3], max_sum[i - 2]) + stairs[i])

print(max_sum[n - 1])