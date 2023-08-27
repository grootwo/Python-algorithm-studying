# Lv.1
# 문자열 내림차순으로 배치하기
def solution(s):
    s_list = sorted(list(s), reverse=True)
    return ''.join(s_list)
