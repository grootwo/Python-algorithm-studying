# Lv.1
# 음양 더하기
def solution(absolutes, signs):
    result = 0
    for i in range(len(signs)):
        if signs[i]:
            result += absolutes[i]
        else:
            result -= absolutes[i]
    return result
