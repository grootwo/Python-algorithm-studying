# 1920
# 수 찾기
import sys

n = int(sys.stdin.readline())
list_n = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
list_m = list(map(int, sys.stdin.readline().split()))

for i in list_m:
    if i in list_n:
        print(1)
    else:
        print(0)