# 10870
# 피보나치 수 5
import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())

def get_fibo(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return get_fibo(num - 1) + get_fibo(num - 2)

print(get_fibo(n))