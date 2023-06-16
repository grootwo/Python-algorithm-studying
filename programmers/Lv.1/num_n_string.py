# Lv.1
# 숫자 문자열과 영단어
from collections import deque
# key: '앞에서 세 글자', value: [총 글자 개수, '숫자']
def solution(s):
    count_dic = {
        'zer': [4, '0'],
        'one': [3, '1'],
        'two': [3, '2'],
        'thr': [5, '3'],
        'fou': [4, '4'],
        'fiv': [4, '5'],
        'six': [3, '6'],
        'sev': [5, '7'],
        'eig': [5, '8'],
        'nin': [4, '9']
    }
    answer = ''
    que = deque(s)
    while que:
        if ord(que[0]) >= 97: # 영단어라면
            temp = ''
            for i in range(3):
                temp += que[i]
            cha = count_dic[temp]
            for i in range(cha[0]):
                que.popleft()
            answer += cha[1]
        else: # 숫자라면
            answer += que.popleft()
    answer = int(answer)
    return answer
