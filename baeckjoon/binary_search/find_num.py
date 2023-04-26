# 1920
# 수 찾기
import sys

n = int(sys.stdin.readline())
list_n = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
list_m = list(map(int, sys.stdin.readline().split()))
list_n.sort()


def binary_search(start, end, num):
    if start > end:
        return 0
    mid = (end + start) // 2
    if num == int(list_n[mid]):
        return 1
    elif num > int(list_n[mid]):
        return binary_search(mid + 1, end, num)
    elif num < int(list_n[mid]):
        return binary_search(start, mid - 1, num)

for i in list_m:
    print(binary_search(0, len(list_n) - 1, i))
