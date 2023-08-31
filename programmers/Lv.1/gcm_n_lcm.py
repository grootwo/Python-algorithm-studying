# Lv.1
# 최대공약수와 최소공배수
def solution(n, m):
    answer = [0, 0]
    if n > m:
        answer[1] = get_least_common_multiple(m, n)
        answer[0] = get_greatest_common_measure(m, n)
    else:
        answer[1] = get_least_common_multiple(n, m)
        answer[0] = get_greatest_common_measure(n, m)
    return answer

def get_greatest_common_measure(num1, num2): # 최대 공약수 구하기
    answer = 0
    for i in range(1, num1 + 1):
        if num1 % i == 0 and num2 % i == 0:
            answer = i
    return answer
    
def get_least_common_multiple(num1, num2): # 최소 공배수 구하기
    i = num2
    while i % num1 != 0 or i % num2 != 0:
        i += num2
    return i
