# Lv.2
# 두 원 사이의 정수 쌍
import math
def solution(r1, r2):
    count = 0
    for i in range(1, r2 + 1):
        y_max = int((r2 ** 2 - i ** 2) ** 0.5)
        y_min = 0 if r1 <= i else math.ceil((r1 ** 2 - i ** 2) ** 0.5)
        count += y_max - y_min + 1
    return (count) * 4
