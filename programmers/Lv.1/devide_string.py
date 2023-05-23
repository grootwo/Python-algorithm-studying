def solution(s):
    first_cha = s[0]
    start = 0
    first_cha_count = 1
    other_cha_count = 0
    answer = []
    for i in range(1, len(s)):
        if first_cha_count == other_cha_count:
            answer.append(s[start:i])
            first_cha = s[i]
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
