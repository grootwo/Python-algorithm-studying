# 18258
# 큐 2
import sys
from collections import deque

queue = deque([])


def push(x):
    queue.append(x)


def pop():
    if len(queue) != 0:
        x = queue.popleft()
        print(x)
        return x
    else:
        print(-1)
        return -1


def size():
    x = len(queue)
    print(x)
    return x


def empty():
    if len(queue) == 0:
        print(1)
        return 1
    else:
        print(0)
        return 0


def front():
    if len(queue) != 0:
        x = queue.popleft()
        print(x)
        queue.appendleft(x)
    else:
        print(-1)


def back():
    if len(queue) != 0:
        x = queue.pop()
        print(x)
        queue.append(x)
    else:
        print(-1)


case = int(input())
for i in range(case):
    answer = sys.stdin.readline().strip()
    if answer[0:4] == 'push':
        push(int(answer[5:]))
    elif answer == 'pop':
        pop()
    elif answer == 'size':
        size()
    elif answer == 'empty':
        empty()
    elif answer == 'front':
        front()
    elif answer == 'back':
        back()