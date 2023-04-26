# 1110
# 더하기 사이클

# 데이터 입력 받기
num = int(input())

num_str = str(num)
if len(num_str) == 2: # 두 자릿수라면
    num1_str = num_str[1]
    num2_str = str(int(num_str[0]) + int(num_str[1]))
    if len(num2_str) == 2:  # 두 자릿수라면
        num2_str = num2_str[1]
else:   # 한 자릿수라면
    num1_str = num_str[0]
    num2_str = num_str[0]
next_str = num1_str + num2_str

count = 1

while num != int(next_str):
    if len(next_str) == 2:  # 두 자릿수라면
        num1_str = next_str[1]
        num2_str = str(int(next_str[0]) + int(next_str[1]))
        if len(num2_str) == 2:  # 두 자릿수라면
            num2_str = num2_str[1]
    else:  # 한 자릿수라면
        num1_str = next_str[0]
        num2_str = next_str[0]
    next_str = num1_str + num2_str
    count += 1

print(count)