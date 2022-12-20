# 11651
# 좌표 정렬하기 2
import sys

count = int(sys.stdin.readline())
xys = []


for i in range(count):
    x, y = map(int, sys.stdin.readline().split())
    xys.append([x, y])

xys.sort(key=lambda x:(x[1], x[0]))

for i in range(count):
    print(xys[i][0], xys[i][1])