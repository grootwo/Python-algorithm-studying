# 1629
# 곱셈
import sys

num, power_num, divider = map(int, sys.stdin.readline().split())


def power(a, b, c):
    if b == 1:
        return a % c
    if b % 2 == 0:
        return (power(a, b//2, c) ** 2) % c
    else:
        return ((power(a, b // 2, c) ** 2) * a) % c


print(power(num, power_num, divider))