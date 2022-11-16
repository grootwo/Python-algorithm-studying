# 1874
# 스택 수열

case = int(input())

nums_list = [int(input()) for _ in range(case)]

stack = []
command_list = [] # 명령어 저장 리스트

def push(x):
    stack.append(x)
    command_list.append('+')


def pop():
    command_list.append('-')
    return stack.pop()


def top():
    if len(stack) != 0:
        return stack[len(stack) - 1]
    else:
        return -1




if command_list.count('NO') != 0:
    print('NO')
else:
    for i in command_list:
        print(i)
# 수열의 인덱스가 바뀔 때마다 스택의 top, 오름차순의 순서를 확인해야 함
# 만약 수열의 인덱스 수가 top이 아닌 스택에 있다면 그것은 불가능함
# 수열의 인덱스가 남아있을 때까지 반복문을 돌려야 함