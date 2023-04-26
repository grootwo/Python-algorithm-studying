# 11720

# 숫자 개수 입력받기
num = int(input())

# 숫자 모두 입력받기
all_num = str(input())

# 숫자 개수만큼 문자열로 변형 후 모두 더하기
sum = 0
for i in range(num):
    sum += int(all_num[i])

print(sum)