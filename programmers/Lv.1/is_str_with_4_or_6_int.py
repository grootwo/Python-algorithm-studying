# Lv.1
# 문자열 다루기 기본
def solution(s):
    try:
        int(s)
        if len(s) != 4 and len(s) != 6:
            return False
        return True
    except:
        return False
