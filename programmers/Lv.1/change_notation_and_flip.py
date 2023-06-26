def solution(n):
    string_n = str(n)
    answer_3 = ''
    temp = 0
    for i in range(len(string_n)):
        temp *= 10
        temp += int(string_n[i])
        print(int(string_n[i]))
        answer_3 += str(temp // 3)
        temp = temp % 3
        print('temp:', temp)
        print('answer_3:', answer_3)
    answer = ''
    return answer
