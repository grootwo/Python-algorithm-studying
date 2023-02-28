# 1927
# 최소 힙
import sys
import heapq as hq

cal_count = int(input())

heap = []
for i in range(cal_count):
    command = int(sys.stdin.readline())
    if command:
        hq.heappush(heap, command)
    else:
        if heap:
            print(hq.heappop(heap))
        else:
            print(0)