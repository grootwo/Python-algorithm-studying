# 9935
# 문자열 폭발
from collections import deque

strings = input()
int_list = list(strings)
popping_string = list(input())
last_ch = popping_string[-1]

que = deque([])

for i in range(len(int_list)):
    if int_list[i] == last_ch and len(que) >= len(popping_string) - 1: # 폭발 문자의 마지막 글자와 같고, 앞의 글자들까지 확인할 정도의 길이가 된다면
        # 폭발 문자와 같은지 확인하기
        check = False
        for j in range(1, len(popping_string)):
            if que[len(que) - j] != popping_string[len(popping_string) - 1 - j]:
                break
        else:
            check = True
        # print("check:", check)
        if check is True: # 폭발 문자와 같다면 삭제
            for j in range(len(popping_string) - 1):
                que.pop()
        else: # 폭발 문자가 아니라면 추가
            que.append(int_list[i])
    else:
        que.append(int_list[i])
    # print(que)

if que:
    print("".join(que))
else:
    print("FRULA")