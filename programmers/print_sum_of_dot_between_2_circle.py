# Lv.2
# 두 원 사이의 정수 쌍
def solution(r1, r2):
    # x^2 + y^2 = r^2
    sum = 0
    for i in range(-r2, r2 + 1):
        for j in range(-r2, r2 + 1):
            # print(i, j)
            if i * i + j * j <= r2 * r2 and i * i + j * j >= r1 * r1:
                sum += 1
                # print("+", i, j)
    answer = sum
    return answer
