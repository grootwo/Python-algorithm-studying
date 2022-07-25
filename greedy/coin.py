# 11047
# 동전 0

import sys

n, price = map(int, input().split())
values = []
for _ in range(n):
    values.append(int(sys.stdin.readline()))

count = 0
leftover = price

if n == 1:
    count += leftover // values[0]
else:
    for i in range(1, n):
        if leftover <= 0:
            break
        count += leftover // values[n - i]
        leftover = leftover % values[n - i]

print(count)