# 9935
# 문자열 폭발
from collections import deque

strings = input()
int_list = list(strings)
popping_string = list(input())
last_ch = popping_string[-1]

que = deque([])

for i in range(len(int_list)):
    if int_list[i] == last_ch and len(que) >= len(popping_string) - 1: # 폭발 문자의 마지막 글자와 같고, 앞의 인덱스를 확일할 정도의 길이가 된다면
        # 확인하기
        check = False
        for j in range(1, len(popping_string)):
            if que[len(que) - j] != popping_string[len(popping_string) - 1 - j]:
                break
        else:
            check = True
        if check is True:
            for j in range(len(popping_string) - 1):
                que.pop()
    else:
        que.append(int_list[i])

if que:
    print("".join(que))
else:
    print("FRULA")