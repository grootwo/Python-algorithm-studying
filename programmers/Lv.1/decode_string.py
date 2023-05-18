# Lv.1
# 둘 만의 암호

def solution(s, skip, index):
    answer = []
    for cha in s:
        now_i = ord(cha)
        check = 1
        i = 1
        while check <= index:
            if now_i + i > 122: # 만약 z 다음이라면 다시 a로
                i -= 26
            next_cha = chr(now_i + i)
            if next_cha in skip:
                i += 1
                continue
            else:
                i += 1
                check += 1
        answer.append(chr(now_i + i - 1))
    answer = ''.join(answer) # string으로 변환
    return answer
