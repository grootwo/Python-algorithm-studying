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
    if start > end:
        return 0
    mid = (end + start) // 2
    if num == int(list_n[mid]):
        return nums_counter[num]
    elif num > int(list_n[mid]):
        return binary_search(mid + 1, end, num)
    elif num < int(list_n[mid]):
        return binary_search(start, mid - 1, num)

for i in list_m:
    print(binary_search(0, len(list_n) - 1, i), end=" ")