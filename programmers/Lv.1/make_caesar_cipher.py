# Lv.1
# 시저 암호
def solution(s, n):
    answer = []
    for cha in s:
        temp = ord(cha)
        if cha != ' ' and temp < 91: # 대문자의 경우
            temp += n
            if temp > 90:
                temp -= 26
        elif cha != ' ' and temp > 96: # 소문자의 경우
            temp += n
            if temp > 122:
                temp -= 26
        answer.append(temp) # 띄어쓰기는 그대로
    return ''.join([chr(i) for i in answer])
