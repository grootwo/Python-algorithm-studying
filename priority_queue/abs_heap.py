# 11286
# 절댓값 힙

import sys
import heapq as hq

cal_count = int(input())

heap = []
for i in range(cal_count):
    command = int(sys.stdin.readline())
    if command:
        hq.heappush(heap, (abs(command), command))
        # print(heap)
    else:
        if heap:
            print(hq.heappop(heap)[1])
        else:
            print(0)