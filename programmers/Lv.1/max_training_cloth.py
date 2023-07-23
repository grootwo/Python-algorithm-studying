def solution(n, lost, reserve):
    for num in reserve:
        if num in lost:
            lost.remove(num)
        elif num - 1 in lost:
            lost.remove(num - 1)
        elif num + 1 in lost:
            lost.remove(num + 1)
    return n - len(lost)
