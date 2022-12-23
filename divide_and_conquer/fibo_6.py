# 11444
# 피보나치 수 6
import sys
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())

def fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return (fibo(num - 1) + fibo(num - 2)) % 1000000007

print(fibo(n))