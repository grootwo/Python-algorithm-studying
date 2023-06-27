# Lv.1
# 3진법 뒤집기
def solution(n):
    answer_3 = ''
    temp = n
    while temp > 0:
        answer_3 += str(temp % 3)
        temp = temp // 3
    answer_10 = 0
    for i in range(1, len(answer_3) + 1):
        answer_10 += int(answer_3[-i]) * (3 ** (i - 1))
    return answer_10
