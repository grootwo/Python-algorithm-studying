# 4949
# 균형잡힌 세상
import sys

stack = []


def push(c):
    stack.append(c)


def pop():
    return stack.pop()


def check_VPS_in_string(string):
    #print(string)
    for i in string:
        #print('i:', i)
        if i == '(' or '[':
            #print(1)
            push(i)
        elif i == ')':
            #print(") rec")
            if stack.pop() != '(':
                #print(2)
                return 'no'
        elif i == ']':
            #print("] rec")
            if stack.pop() != '[':
                #print(3)
                return 'no'
        else:
            continue
    # 모든 문자를 읽었는데 '('나 '['가 남아 있다면
    if len(stack) != 0:
        #print(4)
        return 'no'
    else:
        return 'yes'


#print('(' == ')')
# False인데 같게 인식함

answer = sys.stdin.readline().strip()

while answer != '.':
    print(check_VPS_in_string(answer))
    answer = sys.stdin.readline().strip()
    stack.clear()