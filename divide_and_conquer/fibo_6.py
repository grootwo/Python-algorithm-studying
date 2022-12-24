# 11444
# 피보나치 수 6
import sys
sys.setrecursionlimit(10 ** 9)

n = int(sys.stdin.readline())

# def fibo(num):
#     if num == 0:
#         return 0 % 1000000007
#     elif num == 1:
#         return 1 % 1000000007
#     else:
#         return (fibo(num - 1) + fibo(num - 2)) % 1000000007
#
# print(fibo(n))

fibo = [0] * (n + 1)
fibo[1] = 1
for i in range(2, n + 1):
    fibo[i] = (fibo[i - 1] + fibo[i - 2]) % 1000000007
print(fibo[n])