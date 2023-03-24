# 1655
# 가운데를 말해요
import sys

count = int(input())

int_list = []

for i in range(count):
    num = int(sys.stdin.readline())
    int_list.append(num)
    int_list.sort()
    length = len(int_list)
    if length % 2 == 0:
        print(int_list[length // 2 - 1])
    else:
        print(int_list[length // 2])