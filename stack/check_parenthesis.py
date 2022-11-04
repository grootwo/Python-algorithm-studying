# 9012
# 괄호

stack = []


def push(c):
  stack.append(c)


def pop():
  stack.pop()


def check_VPS(string):
  for i in string:
    if i == '(':
      push(i)
    else:
      # stack이 비어져 있는데 ')'가 입력된다면
      if len(stack) == 0:
        return 'NO'
      else:
        pop()
  # ')'를 모두 짝지었는데 stack에 '('가 남아 있다면
  if len(stack) != 0:
    return 'NO'
  else:
    return 'YES'

case = int(input())

for i in range(case):
  answer = intput().strip()
  print(check_VPS(answer))