def solution(sizes):
    max_w = 0
    max_h = 0
    for i in range(len(sizes)):
        x = min(sizes[i])
        y = max(sizes[i])
        if x > max_w:
            max_w = x
        if y > max_h:
            max_h = y
    answer = max_w * max_h
    return answer
