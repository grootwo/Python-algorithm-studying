# Lv.1
# 예산
def solution(d, budget):
    if sum(d) <= budget: # 모두 사줄 수 있는 경우
        return len(d)
    d.sort()
    for i in range(1, len(d) + 1):
        if sum(d[0:i]) > budget:
            return i - 1
