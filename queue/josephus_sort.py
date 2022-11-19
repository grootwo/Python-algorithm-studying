# 11866
# 요세푸스 문제 0
import sys
from collections import deque

person_count, josephus_num = map(int, input().split())

# queue에 오름차순 순서대로 저장
queue = deque()
for i in range(1, person_count + 1):
    queue.append(i)

print('<', end="")
while len(queue) >= 1:
    for i in range(josephus_num):
        if i != josephus_num - 1:
            num = queue.popleft()
            queue.append(num)
        # 조세푸스 수에 해당되면 출력하기
        else:
            if len(queue) != 1:
                print(queue.popleft(), end=", ")
            # 마지막 수는 반점 출력하지 않기
            else:
                print(queue.popleft(), end="")
print('>')