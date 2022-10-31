# 2941

# 문자열 입력받기
words = list(input())

# 문자열 개수 세기
count_words = len(words)

# while 문으로 반복하기
i = 0
count_croa = 0
while i < count_words:
    char = words[i]
    count_croa += 1
    if i == (count_words - 1):
        break
    if char == 'd':
        if i <= (count_words - 3):
            if (words[i + 1] == 'z') and (words[i + 2] == '='):
                i += 3
            elif words[i + 1] == '-':
                i += 2
            else:
                i += 1
        elif i == (count_words - 2):
            if words[i + 1] == '-':
                i += 2
            else:
                i += 1
        else:
            i += 1
    elif char == 'c':
        if (words[i + 1] == '=') or (words[i + 1] == '-'):
            i += 2
        else:
            i += 1
    elif (char == 'l') or (char == 'n'):
        if words[i + 1] == 'j':
            i += 2
        else:
            i += 1
    elif (char == 's') or (char == 'z'):
        if words[i + 1] == '=':
            i += 2
        else:
            i += 1
    else:
        i += 1

print(count_croa)

# 런타임 에러: 내 생각엔 끝에서 배열 인덱스를 벗어난 것 같다
# 인덱스 마지막에선 확인 하지 말라고 벗어나게 했지만 되지 않네