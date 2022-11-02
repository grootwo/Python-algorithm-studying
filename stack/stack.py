# 10828
# 스택

stack =[]


# push
def func1(x):
  stack.append(x)


# pop
def func2():
 print(stack.pop())


# size
def func3():
  print(len(stack))


# empty
def func4():
  if len(stack) != 0:
    print(0)
  else:
    print(1)


def top():
  if len(stack) != 0:
    print(stack[len(stack) - 1])
  else:
    print(-1)




while True()