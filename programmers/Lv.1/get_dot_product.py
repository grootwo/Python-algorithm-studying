# Lv.1
# 내적
def solution(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    # return sum([num1 * num2 for num1, num2 in zip(a,b)])
    return result
