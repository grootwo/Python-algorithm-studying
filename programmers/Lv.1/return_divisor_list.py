# Lv.1
# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    if answer:
        answer.sort()
        return answer
    else:
        return [-1]
