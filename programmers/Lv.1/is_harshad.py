# Lv.1
# 하샤드 수
def solution(x):
    temp = str(x)
    result = 0
    for cha in temp:
        result += int(cha)
    if x % result == 0:
        return True
    else:
        return False
