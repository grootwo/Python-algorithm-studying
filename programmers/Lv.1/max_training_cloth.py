def solution(n, lost, reserve):
    count = len(lost)
    for i in lost:
        if i - 1 in reserve:
            reserve.remove(i - 1)
            count -= 1
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            count -= 1
    answer = n - count
    return answer
