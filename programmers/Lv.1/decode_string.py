def solution(s, skip, index):
    # how to initate alphabet
    answer = []
    for cha in s:
        now_i = ord(cha)
        check = 1
        i = 1
        while check <= index:
            if chr(now_i + i) in skip:
                i += 1
                continue
            else:
                i += 1
                check += 1
        if now_i + i > 122:
            answer.append(chr(now_i + i - 27))
        else:
            answer.append(chr(now_i + i - 1))
    answer = ''.join(answer)
    return answer
