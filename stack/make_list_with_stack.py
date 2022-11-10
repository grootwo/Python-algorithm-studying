# 1874
# 스택 수열

case = int(input())

nums_list = [int(input()) for _ in range(case)]

stack = []

def push(x):
    print('+')
    stack.append(x)


def pop():
    print('-')
    return stack.pop()


def top():
    return stack[len(stack) - 1]
# 자신의 순서라면 pop()
# 할 수 있는 경우:
#   1. 제일 마지막 원소가 해당 순서

# 수열의 인덱스
list_i = 0
for i in range(1, case + 1):
    if i == nums_list[list_i]:
        push(i)
        pop()
        list_i += 1
    else:
        push(i)