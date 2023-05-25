# Lv.2
# 점 찍기
import math
def solution(k, d):
    result = 0
    for i in range(0, d + 1, k):
        result += math.floor(math.sqrt(d ** 2 - i ** 2)) // k + 1
    answer = result
    return answer