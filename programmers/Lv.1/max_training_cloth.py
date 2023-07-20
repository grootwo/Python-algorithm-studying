def solution(n, lost, reserve):
    for i in lost:
        if i - 1 in reserve:
            reserve.remove(i - 1)
            lost.remove(i)
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            lost.remove(i)
        print(lost, reserve)
    answer = n - len(lost)
    return answer
