# 5430
# AC
import sys
from collections import deque

case = int(input())


def R(array):
    array.reverse()
    return array


def D(array):
    if len(array) != 0:
        array.popleft()
        return array
    else:
        print('error')
        return False


for i in range(case):
    funcs = input()
    nums_count = int(input())
    if nums_count == 0:
        nums_list = []
    else:
        nums_list_input = input()
        nums_list = list(map(int, nums_list_input[1:-1].split(',')))
    nums_queue = deque(nums_list)
    for j in funcs:
        if j == 'R':
            nums_queue = R(nums_queue)
        else:
            nums_queue = D(nums_queue)
            if nums_queue == False:
                break
    if nums_queue != False:
        print('[', end='')
        for j in range(len(nums_queue)):
            print(nums_queue[j], end='')
            if j != len(nums_queue) - 1:
                print(',', end='')
        print(']')