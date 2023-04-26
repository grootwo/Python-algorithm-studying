# 1546
# 평균

count = int(input())
grade = list(map(int, input().split()))
max_grade = max(grade)

sum = 0
for i in range(count):
    grade[i] = grade[i] / max_grade * 100
    sum += grade[i]

print(sum / count)