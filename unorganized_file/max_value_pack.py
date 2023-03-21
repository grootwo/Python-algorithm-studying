# 12865
# 평범한 배낭
import sys

things = []
things_count, max_kg = map(int, sys.stdin.readline().split())
for i in range(things_count):
    kg, value = map(int, sys.stdin.readline().split())
    things.append([kg, value])

# value 기준 정렬
things.sort(key=lambda x: (-x[1], x[0]))
print(things)

# kg 기준 겅렬
things.sort(key=lambda x: (x[0], -x[1]))
print(things)