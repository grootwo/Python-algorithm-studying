def solution(s):
    strings = list(map(list, s.split(' ')))
    print(strings)
    # for string in strings:
    #     for i in range(len(string)):
    #         if i % 2 == 0: # 홀수 번째 문자
    #             string[i] = string[i].lower()
    #         else: # 짝수 번째 문자
    #             string[i] = string[i].upper()
    return ' '.join(strings)
