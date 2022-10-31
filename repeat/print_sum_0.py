# 10952
# A+B - 5
import sys

num1, num2 = map(int, sys.stdin.readline().split())

while num1 != 0 and num2 != 0:
    print(num1 + num2)
    num1, num2 = map(int, sys.stdin.readline().split())
