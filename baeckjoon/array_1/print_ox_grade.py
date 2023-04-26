# 8958
# OX퀴즈
import sys

count = int(input())

results_ox = []
for i in range(count):
    results_ox.append(sys.stdin.readline().strip())


def count_grade(result):
    grade = 0
    plus = 1
    for i in result:
        if i == 'O':
            grade += plus
            plus += 1
        else:
            plus = 1
    return grade

resuts_grade = []
for i in results_ox:
    resuts_grade.append(count_grade(i))

for i in resuts_grade:
    print(i)