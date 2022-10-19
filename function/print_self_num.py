# 4673
# 셀프 넘버
from collections import deque

nums = [None] * 10001

queue = deque()

for i in range(1, 10001):
    queue.append(i)
    while queue:
        x = queue.popleft()
        x_str = str(x)
        sum = x
        for j in x_str:
            sum += int(j)
        if sum <= 10000:
            nums[sum] = True
            queue.append(sum)

for i in range(1, 10001):
    if nums[i] is None:
        print(i)