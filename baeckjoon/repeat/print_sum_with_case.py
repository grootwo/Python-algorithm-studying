# 11021
# A+B - 7

import sys

count = int(input())

num1s = []
num2s = []

for i in range(count):
    num1, num2 = map(int, sys.stdin.readline().split())
    num1s.append(num1)
    num2s.append(num2)

for i in range(count):
    print("Case #" + str(i + 1) + ": " + str(num1s[i] + num2s[i]))
