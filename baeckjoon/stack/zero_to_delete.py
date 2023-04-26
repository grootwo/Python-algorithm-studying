# 10773
# 제로

stack =[]


def push(x):
  stack.append(x)


def pop():
  return stack.pop()


def size():
  print(len(stack))


def empty():
  if len(stack) != 0:
    print(0)
  else:
    print(1)


def top():
  if len(stack) != 0:
    print(stack[len(stack) - 1])
  else:
    print(-1)


case = int(input())

for i in range(case):
  n = int(input())
  if n == 0:
    pop()
  else:
    push(n)

result = 0
while len(stack) != 0:
  result += pop()

print(result)