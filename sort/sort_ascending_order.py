# 2750
# 수 정렬하기

case = int(input())
nums_list = list(int(input()) for _ in range(case))

for i in range(case - 1):
    for j in range(case - 1 - i):
        if nums_list[j] > nums_list[j + 1]:
            temp = nums_list[j]
            nums_list[j] = nums_list[j + 1]
            nums_list[j + 1] = temp

for i in nums_list:
    print(i)