# 10816
# 숫자 카드 2
import sys
from collections import Counter

# key를 찾을 수 있도록 문자로 변경해야 함

n = int(sys.stdin.readline())
list_n = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
list_m = list(map(int, sys.stdin.readline().split()))
list_n.sort()
nums_counter = Counter(list_n)


def binary_search(start, end, num):
    # print('start, end, num:', start, end, num)
    if start == end:
        if num == int(list_n[start]):
            print(nums_counter[num], end=' ')
            return
        else:
            print(0, end=' ')
            return
    elif start > end:
        print(0, end=' ')
        return
    else:
        mid = (end + start) // 2
        # print('mid num:', mid, list_n[mid])
        if num == int(list_n[mid]):
            print(nums_counter[num], end=' ')
        elif num > int(list_n[mid]):
            binary_search(mid + 1, end, num)
        elif num < int(list_n[mid]):
            binary_search(start, mid - 1, num)

for i in list_m:
    binary_search(0, len(list_n), i)