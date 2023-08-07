def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    d.sort()
    # 모든 부서에 사줄 수 없는 경우도 있나?
    for i in range(1, len(d) + 1):
        if sum(d[0:i]) > budget:
            return i - 1
