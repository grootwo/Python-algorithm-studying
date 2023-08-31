# Lv.1
# 최대공약수와 최소공배수
def solution(n, m):
    answer = [0, 0]
    if n > m:
        answer[1] = get_greatest_common_measure(m, n)
        answer[0] = get_least_common_multiple(m, n)
    else:
        answer[1] = get_greatest_common_measure(n, m)
        answer[0] = get_least_common_multiple(n, m)
    return answer

def get_least_common_multiple(num1, num2):
    answer = 0
    for i in range(1, num1 + 1):
        if num1 % i == 0 and num2 % i == 0:
            answer = i
    return answer
    
def get_greatest_common_measure(num1, num2):
    i = num2
    while i % num1 != 0 or i % num2 != 0:
        i += 1
    return i
