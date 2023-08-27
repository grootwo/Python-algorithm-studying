# Lv.1
# 두 정수 사이의 합
def solution(a, b):
    if a > b:
        big, small = a, b
    else:
        big, small = b, a
    big_sum = big * (big + 1) / 2 # 큰 수의 등차수열
    small_sum = (small - 1) * (small) / 2 # 작은 수 -1의 등차수열
    return big_sum - small_sum
