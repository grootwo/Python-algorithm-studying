# 1920
# 수 찾기
import sys

n = int(sys.stdin.readline())
list_n = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
list_m = list(map(int, sys.stdin.readline().split()))
list_n.sort()


def binary_search(start, end, num):
    if start == end:
        if num == list_n[start]:
            print(1)
            return
        else:
            print(0)
            return
    elif start > end:
        print(0)
    else:
        mid = (end + start) // 2
        if num == list_n[mid]:
            print(1)
            return
        elif num > list_n[mid]:
            binary_search(mid + 1, end, num)
        elif num < list_n[mid]:
            binary_search(start, mid - 1, num)


for i in list_m:
    binary_search(0, len(list_n) - 1, i)
