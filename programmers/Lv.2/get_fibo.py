def solution(n):
    n = n % 1234567
    return get_fibo(n) % 1234567

def get_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return get_fibo(n - 1) + get_fibo(n - 2)
