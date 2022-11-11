# 18258
# 큐 2
from collections import deque

queue = deque([])


def push(x):
    queue.append(x)


def pop():
    x = queue.popleft()
    print(x)
    return x


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
        print(queue.index(0))
    else:
        print(-1)


def back():
    if len(queue) != 0:
        print(queue.index(len(queue) - 1))
    else:
        print(-1)