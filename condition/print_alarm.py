# 2884
# 알람 시계

hour_c, min_c = map(int, input().split())

min_a = min_c - 45
hour_a = hour_c

if min_a < 0:
    min_a = 60 - abs(min_a)
    hour_a -= 1
if hour_a < 0:
    hour_a = 24 - abs(hour_a)

print(hour_a, min_a)
