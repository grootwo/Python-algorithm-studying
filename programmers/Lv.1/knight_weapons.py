# Lv.1
# 기사단원의 무기
def solution(number, limit, power):
    answer = [0] * number
    for i in range(1, number + 1):
        for j in range(1, int(i ** (1/2) + 1)):
            if i % j == 0 and j * j != i:
                answer[i - 1] += 2
            elif j * j == i:
                answer[i - 1] += 1
    # print(answer)
    for i in range(number):
        if answer[i] > limit:
            answer[i] = power
    # print(answer)
    return sum(answer)
