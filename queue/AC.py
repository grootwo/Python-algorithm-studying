# 5430
# AC
import sys
from collections import deque

case = int(input())


def R(array):
    array.reverse()
    return array


def D(array):
    if array:
        array.popleft()
        return array
    else:
        return False


for i in range(case):
    funcs = input()
    nums_count = int(input())
    # 리스트 입력받기
    if nums_count == 0:
        nums_list_input = input()
        nums_list = []
    else:
        nums_list_input = input()
        nums_list = list(map(int, nums_list_input[1:-1].split(',')))
    nums_queue = deque(nums_list)
    # 명령 실행하기
    for j in funcs:
        if j == 'R':
            nums_queue = R(nums_queue)
        else:
            nums_queue = D(nums_queue)
            if nums_queue is False:
                break
    # 결과 출력하기
    if nums_queue is not False:
        print('[', end='')
        while nums_queue:
            if len(nums_queue) > 1:
                print(nums_queue.popleft(), end='')
                print(',', end='')
            else:
                print(nums_queue.popleft(), end='')
        print(']')
    else:
        print('error')