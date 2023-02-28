# 11279
# 최대 힙

# 힙이란, 완전 이진 트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조라고 한다
# 여러 값들 중에 최댓값이나 최솟값을 빠르게 찾아낼 수 있다고 한다

# 최대 힙: 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 완전 이진 트리
import sys
import heapq as hq

cal_count = int(input())

heap = []
for i in range(cal_count):
    command = int(sys.stdin.readline())
    if command:
        hq.heappush(heap, (-command, command))
    else:
        if heap:
            print(hq.heappop(heap)[1])
        else:
            print(0)
