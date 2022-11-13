# 4949
# 균형잡힌 세상
import sys

stack = []


def push(c):
    stack.append(c)


def pop():
    return stack.pop()


def check_VPS_in_string(string):
    for i in string:
        if i == '(' or i == '[':
            push(i)
        elif i == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return 'no'
        elif i == ']':
            if len(stack) == 0 or stack.pop() != '[':
                return 'no'
        else:
            continue
    # 모든 문자를 읽었는데 '('나 '['가 남아 있다면
    if len(stack) != 0:
        return 'no'
    else:
        return 'yes'


answer = input()

while answer != ".":
    print(check_VPS_in_string(answer))
    # 데이터, stack 초기화
    answer = input()
    stack.clear()