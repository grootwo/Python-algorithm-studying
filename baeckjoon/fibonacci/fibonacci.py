# 24416
# 피보나치 수열

# 시간 초과로 인해 지우고 pypy3로 제출
# import sys
# sys.setrecursionlimit(10 ** 6)

answer = int(input())


def fib1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fib1(n - 1) + fib1(n - 2))


def fib2(n):
    count2 = 0
    f = [None] * (n + 1)
    f[1] = 1
    f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        count2 += 1
    return count2


print(fib1(answer), fib2(answer))

# def fib2(n):
#     global count2
#     f = [1, 1, 0]
#     i = 2
#     while i < n:
#         f[2] = f[0] + f[1]
#         f[0] = f[1]
#         f[1] = f[2]
#         i += 1
#         count2 += 1
#     return f[2]

# queue 사용
# def fib2(n):
#     global count2
#     queue = deque([1, 1])
#     i = 2
#     while i < n:
#         temp1 = queue.popleft()
#         temp2 = queue.popleft()
#         queue.append(temp1 + temp2)
#         queue.appendleft(temp2)
#         i += 1
#         count2 += 1
#     return queue.pop()