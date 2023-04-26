# 14681
# 사분면 고르기
import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

if x > 0 and y > 0:
    quadrant = 1
elif x < 0 and y > 0:
    quadrant = 2
elif x < 0 and y < 0:
    quadrant = 3
else:
    quadrant = 4

print(quadrant)