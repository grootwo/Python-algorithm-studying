# Lv.1
# 이상한 문자 만들기
def solution(s):
    strings = list(map(list, s.split(' ')))
    for string in strings:
        for i in range(len(string)):
            if i % 2 == 1: # 홀수 번째 문자
                string[i] = string[i].lower()
            else: # 짝수 번째 문자
                string[i] = string[i].upper()
    return ' '.join([''.join(str) for str in strings])
