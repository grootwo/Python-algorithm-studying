def solution(t, p):
    length = len(p)
    count = 0
    for i in range(0, len(t) - length + 1):
        # print(int(t[i:i + length]))
        if int(t[i:i + length]) <= int(p):
            # print("+")
            count += 1
    answer = count
    return answer
