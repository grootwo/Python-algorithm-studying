# 1904

n = int(input())

# 타일 개수 하나하나 세아려 보니 피보나치와 같음


def fib(n):
    f = [None] * (1000001)
    f[1] = 1
    f[2] = 2
    for i in range(3, n + 1):
        f[i] = (f[i - 1] + f[i - 2]) % 15746
    return f[n]


result = fib(n)
print(result)

# 배열로 하면 메모리 초과
# 큐로 하면 시간 초과
# 반복문 때문에 잘 안 되는 건가?

# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         queue = deque([1, 2])
#         for i in range(3, n + 1):
#             temp1 = queue.popleft()
#             temp2 = queue.popleft()
#             queue.append(temp1 + temp2)
#             queue.appendleft(temp2)
#         return queue.pop()