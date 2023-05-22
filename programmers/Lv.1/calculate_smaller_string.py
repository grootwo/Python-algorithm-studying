# Lv.1
# 크기가 작은 부분문자열
def solution(t, p):
    length = len(p)
    count = 0
    for i in range(0, len(t) - length + 1):
        if int(t[i:i + length]) <= int(p):
            count += 1
    answer = count
    return answer
