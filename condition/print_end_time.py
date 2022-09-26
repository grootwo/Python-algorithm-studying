# 2525
# 오븐 시계

hour_c, min_c = map(int, input().split())
time = int(input())

min_e = min_c + time
hour_e = hour_c

if min_e >= 60:
    hour_e += int(min_e / 60)
    min_e -= 60 * int(min_e / 60)
if hour_e >= 24:
    hour_e -= 24

print(hour_e, min_e)