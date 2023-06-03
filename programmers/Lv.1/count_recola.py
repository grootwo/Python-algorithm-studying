# Lv,1
# 콜라 문제
def solution(a, b, n):
    cola = n
    count = 0
    while cola >= a:
        temp = cola // a
        count += temp * b
        cola = cola % a + temp * b
    answer = count
    return answer
