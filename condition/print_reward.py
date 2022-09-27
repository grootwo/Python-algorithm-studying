# 2480
# 주사위 세개

num1, num2, num3 = map(int, input().split())

same_num = 0
count = 0

# 같은 눈의 개수와 값 알기
if num1 == num2:
    count += 1
    same_num = num1
if num2 == num3:
    count += 1
    same_num = num2
if num1 == num3:
    count += 1
    same_num = num3

# 같은 눈이 3개 나오는 경우
if count == 3:
    reward = 10000 +
# 같은 눈이 2개 나오는 경우

# 같은 눈이 없는 경우