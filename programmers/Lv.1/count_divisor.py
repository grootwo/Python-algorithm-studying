# Lv.1
# 약수의 개수와 덧셈
def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        temp = num ** 0.5
        if int(temp) == temp:
            answer -= num
        else:
            answer += num
    return answer
