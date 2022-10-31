# 11047
# 동전 0

import sys

n, leftover = map(int, input().split())
values = []
for _ in range(n):
    values.append(int(sys.stdin.readline()))

count = 0
for i in reversed(range(n)):
    count += leftover // values[i]
    leftover = leftover % values[i]

print(count)

# for i in range(1, n):
#     if leftover <= 0:
#         break
#     count += leftover // values[n - i]
#     leftover = leftover % values[n - i]