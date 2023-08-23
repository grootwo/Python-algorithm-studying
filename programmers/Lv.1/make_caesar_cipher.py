def solution(s, n):
    answer = []
    for cha in s:
        if cha != ' ':
            temp = ord(cha) + n
            if temp > 122:
                temp -= 26
            answer.append(temp)
        else:
            answer.append(' ')
    return ''.join([chr(i) for i in answer])
