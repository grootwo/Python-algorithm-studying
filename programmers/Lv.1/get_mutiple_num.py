# Lv.1
# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = []
    for i in range(x, x*n + 1, x):
        answer.append(i)
    return answer
