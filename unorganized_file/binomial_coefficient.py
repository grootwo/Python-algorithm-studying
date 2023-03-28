# 11401
# 이항 계수 3
import sys

sys.setrecursionlimit(10**6)

n, k = map(int, input().split())

result_n = 1
for i in range(k):
    result_n *= (n - i)

result_k = 1
for i in range(k):
    result_k *= (k - i)

result = int(result_n / result_k) % 1000000007
print(int(result))