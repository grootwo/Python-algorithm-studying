# 17298
# 오큰수

import sys

count = int(input())
int_list = list(map(int, sys.stdin.readline().split()))

for i in range(len(int_list)):
    check = False
    for j in range(i + 1, len(int_list)):
        if int_list[i] < int_list[j]:
            print(int_list[j], end=" ")
            check = True
            break
    if check is False:
        print(-1, end=" ")