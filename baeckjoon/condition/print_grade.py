# 9498
# 시험 성적

num = int(input())

num = num / 10

if num >= 9:
    grade = 'A'
elif num >= 8:
    grade = 'B'
elif num >= 7:
    grade = 'C'
elif num >= 6:
    grade = 'D'
else:
    grade = 'F'

print(grade)