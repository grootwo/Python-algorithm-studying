# 11401
# 이항 계수 3
import sys

sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
check = 0


def factorial(num):
    global check
    # print("num and check", num, check)
    if check >= k - 1:
        return num
    check += 1
    if num == 1:
        return 1
    else:
        return factorial(num - 1) * num


result = int(factorial(n))
check = 0
result /= int(factorial(k))
result %= 1000000007
print(int(result))