# Lv.1
# 문자열 내 p와 y의 개수
def solution(s):
    if s.count('p') + s.count('P') == s.count('y') + s.count('Y'):
        return True
    return False
