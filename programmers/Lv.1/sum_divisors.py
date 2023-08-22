# Lv.1
# 약수의 합
def solution(n):
    result = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0: # 약수라면
            if i * i != n: # 제곱근이 아니라면
                result += (n // i)
            result += i
    return result
