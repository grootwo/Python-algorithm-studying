# 11444
# 피보나치 수 6
import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)

n = int(sys.stdin.readline())

# def fibo(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return (fibo(num - 1) + fibo(num - 2)) % 1000000007

def fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        que = deque([0, 1])
        for _ in range(num - 1):
            result = que[0] + que[1]
            que.popleft()
            que.append(result)
        return que[1] % 1000000007

print(fibo(n))