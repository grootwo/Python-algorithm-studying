# 5622

# 단어 입력받기
words = input()

# 단어 별 숫자 더하기
count = 0
for i in range(len(words)):
    char = words[i]
    code = ord(char)
    if 65 <= code <= 67:
        count += 3
    elif 68 <= code <= 70:
        count += 4
    elif 71 <= code <= 73:
        count += 5
    elif 74 <= code <= 76:
        count += 6
    elif 77 <= code <= 79:
        count += 7
    elif 80 <= code <= 83:
        count += 8
    elif 84 <= code <= 86:
        count += 9
    else:
        count += 10

print(count)