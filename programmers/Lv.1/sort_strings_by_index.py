# Lv.1
# 문자열 내 마음대로 정렬하기
def solution(strings, n):
    strings.sort(key=lambda x: (x[n], x))
    return strings
