def solution(n, lost, reserve):
    count = 0
    for num in lost:
        if num - 1 in reserve:
            reserve.remove(num - 1)
            count += 1
        elif num + 1 in reserve:
            reserve.remove(num + 1)
            count += 1
    return n - len(lost) + count
