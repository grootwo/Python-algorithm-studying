# LV.1
# 문자열 나누기
def solution(s):
    first_cha = s[0]
    start = 0
    first_cha_count = 1
    other_cha_count = 0
    answer = []
    for i in range(1, len(s)):
        if first_cha_count == other_cha_count:
            answer.append(s[start:i]) # 문자열 추가하기
            first_cha = s[i] # 다음 문자부터 인덱싱하기
            first_cha_count = 0
            other_cha_count = 0
            start = i
        if s[i] == first_cha:
            first_cha_count += 1
        else:
            other_cha_count += 1
    if first_cha_count != 0:
        answer.append(s[start:])
    return len(answer)
