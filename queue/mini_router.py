# 15828
# Router
import sys
from collections import deque

# 양의 정수가 들어오면 프로세스
# 0이 들어오면 앞에서 프로세스 하나씩 처리
# -1은 입력의 끝
# 마지막으로 남은 프로세스 모두 출력

buffer_limit = int(input())

queue = deque([])

answer = int(input())
while answer != -1:
    if answer > 0:
        if len(queue) < buffer_limit:  
          queue.append(answer)
    elif answer == 0:
        queue.popleft()
    answer = int(input())

if len(queue) != 0:
    for i in queue:
        print(i, ' ', end="")
else:
    print('empty')