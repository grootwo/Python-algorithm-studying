# 10866
# 덱
import sys
from collections import deque

my_deque = deque([])


def push_front(x):
    my_deque.appendleft(x)


def push_back(x):
    my_deque.append(x)


def pop_front():
    if len(my_deque) != 0:
        x = my_deque.popleft()
        print(x)
        return x
    else:
        print(-1)
        return -1


def pop_back():
    if len(my_deque) != 0:
        x = my_deque.pop()
        print(x)
        return x
    else:
        print(-1)
        return -1


def size():
    x = len(my_deque)
    print(x)
    return x


def empty():
    if len(my_deque) == 0:
        print(1)
        return 1
    else:
        print(0)
        return 0


def front():
    if len(my_deque) != 0:
        print(my_deque[0])
    else:
        print(-1)


def back():
    if len(my_deque) != 0:
        print(my_deque[-1])
    else:
        print(-1)


case = int(input())
for i in range(case):
    answer = sys.stdin.readline().strip()
    if answer[0:10] == 'push_front':
        push_front(int(answer[11:]))
    elif answer[0:9] == 'push_back':
        push_back(int(answer[10:]))
    elif answer == 'pop_front':
        pop_front()
    elif answer == 'pop_back':
        pop_back()
    elif answer == 'size':
        size()
    elif answer == 'empty':
        empty()
    elif answer == 'front':
        front()
    elif answer == 'back':
        back()