# 10872
# 팩토리얼
import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())


def get_factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * get_factorial(num - 1)


print(get_factorial(n))