# 10828
# 스택
import sys

stack =[]


# push
def func1(x):
  stack.append(x)


# pop
def func2():
  if len(stack) == 0:
    print(-1)
  else:
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


# top
def func5():
  if len(stack) != 0:
    print(stack[len(stack) - 1])
  else:
    print(-1)


case = int(input())

for i in range(case):
  answer = sys.stdin.readline().strip()
  if answer[0:4] == 'push':
    func1(int(answer[5:]))
  elif answer == 'pop':
    func2()
  elif answer == 'size':
    func3()
  elif answer == 'empty':
    func4()
  elif answer == 'top':
    func5()