# 17298
# 오큰수

# 시간 복잡도 O(n) 사용해야 한다

import sys

count = int(sys.stdin.readline())
int_list = list(map(int, sys.stdin.readline().split()))

answer = [-1] * count
stack = []

for i in range(count):
    while stack and stack[-1][0] < int_list[i]:
        temp, index = stack.pop()
        answer[index] = int_list[i]
    stack.append([int_list[i], i])

print(*answer)