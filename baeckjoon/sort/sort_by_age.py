# 10814
# 나이순 정렬
import sys

count = int(sys.stdin.readline())

infos = []
for i in range(count):
    age, name = sys.stdin.readline().split()
    infos.append([int(age), name])

infos.sort(key=lambda x:x[0])

for i in range(count):
    print(infos[i][0], infos[i][1])