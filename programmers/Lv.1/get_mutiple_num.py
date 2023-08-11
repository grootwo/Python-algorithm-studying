# Lv.1
# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = []
    check = 1 if x > 0 else -1
    for i in range(x, x * n + check, x):
        answer.append(i)
    return answer
