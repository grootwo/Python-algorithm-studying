# 1874
# 스택 수열

case = int(input())

nums_list = []
for i in range(case):
    nums_list.append(int(input()))

stack = []
command_list = [] # 명령어 저장 리스트
check = True # 가능 여부 체크 변수


def push(x):
    stack.append(x)
    command_list.append('+')


def pop():
    if len(stack) != 0:
        command_list.append('-')
        return stack.pop()
    else:
        return -1


def top():
    if len(stack) != 0:
        return stack[len(stack) - 1]
    else:
        return -1


num = 1
for i in nums_list:
    # 만약 불가능하다면 반복문 종료
    if check is False:
        break
    while check is True:
        if num < i:
            push(num)
            num += 1
        elif num == i:
            push(num)
            pop()
            num += 1
            break
        else:
            if pop() != i:
                check = False
            else:
                break


if check is False:
    print('NO')
else:
    for i in command_list:
        print(i)
# 수열의 인덱스가 바뀔 때마다 스택의 top, 오름차순의 순서를 확인해야 함
# 만약 수열의 인덱스 수가 top이 아닌 스택에 있다면 그것은 불가능함
# 수열의 인덱스가 남아있을 때까지 반복문을 돌려야 함