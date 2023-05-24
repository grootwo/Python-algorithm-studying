# Lv.2
# 점 찍기
def solution(k, d):
    result = []
    for i in range(0, d + 1, k):
        for j in range(0, d + 1, k):
            if i ** 2 + j ** 2 <= d ** 2:
                # print(i, j)
                result.append((i, j))
    answer = len(result)
    return answer