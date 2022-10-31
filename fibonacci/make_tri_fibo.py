# 9461

# 정삼각형의 변의 길이는 바로 이전이 아닌, 이전의 이전과 이전의 이전의 이전의 길이를 더한 값과 같다


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        f = [None] * (n + 1)
        f[0] = 0
        f[1] = 1
        f[2] = 1
        for i in range(3, n + 1):
            f[i] = f[i - 2] + f[i - 3]
        return f[n]


t = int(input())
for _ in range(t):
    n = int(input())
    print(fib(n))