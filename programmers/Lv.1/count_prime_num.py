# Lv.1
# 소수 찾기
def solution(n):
    count = 0
    for num in range(1, n + 1):
        count += is_prime(num)
    return count

def is_prime(num):
    if num == 0 or num == 1:
        return 0
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return 0
    return 1
