# 5430
# AC
# 참고(https://hongcoding.tistory.com/44)
import sys
from collections import deque

case = int(input())

for i in range(case):
    # 데이터 입력받기
    funcs = sys.stdin.readline().rstrip()
    nums_count = int(sys.stdin.readline())
    if nums_count == 0:
        temp = sys.stdin.readline().rstrip()
        nums_queue = deque([])
    else:
        nums_list = sys.stdin.readline().rstrip()[1:-1].split(',')
        nums_queue = deque(nums_list)
    check = False # 에러 여부 확인 변수
    R_count = 0
    # 명령 실행하기
    for j in funcs:
        if j == 'R':
            R_count += 1
        elif j == 'D':
            if len(nums_queue) != 0:
                if R_count % 2 == 0:
                    nums_queue.popleft()
                else:
                    nums_queue.pop()
            else:
                check = True
                print('error')
                break
    # 결과 출력하기
    if check is False:
        if R_count % 2 == 1:
            nums_queue.reverse()
        print('[' + ','.join(nums_queue) + ']')