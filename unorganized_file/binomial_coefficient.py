# 11401
# 이항 계수 3
import sys

sys.setrecursionlimit(10**6)

n, k = map(int, input().split())

def factorial(num):
    if num == 1:
        return 1
    else:
        return factorial(num - 1) * num

result = int(factorial(n) / factorial(k)) % 1000000007
print(result)