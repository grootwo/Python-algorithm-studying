# Lv.1
# 최소직사각형
def solution(sizes):
    max_w = 0
    max_h = 0
    for size in sizes:
        x = min(size)
        y = max(size)
        if x > max_w:
            max_w = x
        if y > max_h:
            max_h = y
    answer = max_w * max_h
    return answer
