def solution(s):
    for i in s:
        if '0' > i or '9' < i:
            return False
    return True
