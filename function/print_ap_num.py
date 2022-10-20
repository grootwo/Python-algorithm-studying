# 1065
# 한수

num = int(input())
count = 0

# 1부터 num까지 확인
for i in range(1, num + 1):
    num_str = str(i)
    # 두자릿수까지는 모두 등차수열
    if len(num_str) == 1 or len(num_str) == 2:
        count += 1
    # 세자릿수부터 각자리별로 등차수열 확인
    else:
        for j in range(2, len(num_str)):
            sub1 = int(num_str[j]) - int(num_str[j - 1])
            sub2 = int(num_str[j - 1]) - int(num_str[j - 2])
            if sub1 != sub2:
                break
            if j == len(num_str) - 1:
                count += 1

print(count)