# 10430
# 나머지

import sys

a, b, c = map(int, sys.stdin.readline().split())
result = []

result.append((a + b) % c)
result.append(((a % c) + (b % c)) % c)
result.append((a * b) % c)
result.append(((a % c) * (b % c)) % c)

for i in result:
    print(i)