# Lv.1
# 약수의 개수와 덧셈
def solution(left, right):
    int_list = [0] * (right - left + 1)
    # 약수의 개수 구하기
    for i in range(1, right + 1):
        for j in range(left, right + 1):
            if j >= i and j % i == 0:
                int_list[j - left] += 1
    # 결괏값 구하기
    answer = 0
    for i in range(left, right + 1):
        if int_list[i - left] % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
