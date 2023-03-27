# 11401
# 이항 계수 3
import sys

sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
check = 0


def factorial(num):
    global check
    print("num and check", num, check)
    if check >= k:
        return num
    check += 1
    if num == 1:
        return 1
    else:
        return factorial(num - 1) * num


result = int(factorial(n) / factorial(k)) % 1000000007
print(result)