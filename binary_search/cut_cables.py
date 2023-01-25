# 1654
# 랜선 자르기
# 참고 (https://claude-u.tistory.com/443)
import sys

cable_count, need = map(int, input().split())
cables = [int(sys.stdin.readline()) for _ in range(cable_count)]
start, end = 1, max(cables)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in cables:
        count += i // mid

    if count >= need:
        start = mid + 1
    else:
        end = mid - 1

print(end)