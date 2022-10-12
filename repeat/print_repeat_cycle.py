# 1110
# 더하기 사이클

# 데이터 입력 받기
num = int(input())

num_str = str(num)
if len(num_str) == 2:
    next = int(num_str[0]) + int(num_str[1])
else:
    next = num

count = 1

# 반복문 통해
while next != num:
    next_str = str(next)
    # 한 자릿수라면
    if len(num_str) == 2:
        next = int(num_str[0]) + int(num_str[1])
    # 두 자릿수라면
    else:
        next =

# 다음 숫자 = 이전 숫자[1] + (이전 숫자[0] + 이전 숫자[1])[1]
# 다음 숫자 만들기
# 현재와 비교하기
# 세기

print(count)