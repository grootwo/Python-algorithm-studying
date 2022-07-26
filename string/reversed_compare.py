# 2908

# 정수 두 개 입력받기
num1, num2 = input().split()

# 정수 두 개 각각 뒤집어서 저장
num1 = int(num1[::-1])
num2 = int(num2[::-1])

# 두 정수 비교 후 큰 수 출력
if num1 > num2:
    print(num1)
else:
    print(num2)