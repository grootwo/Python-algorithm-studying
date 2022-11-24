# 2750
# 수 정렬하기

case = int(input())
nums_list = list(int(input()) for _ in range(case))

for i in range(case - 1):
    # print('i', i)
    for j in range(case - 1 - i):
        # print('j', j)
        if nums_list[j] > nums_list[j + 1]:
            temp = nums_list[j]
            nums_list[j] = nums_list[j + 1]
            nums_list[j + 1] = temp
        elif nums_list[j] == nums_list[j + 1]:
            nums_list[j] = False
        # print(nums_list)

count = nums_list.count(False)
if count >= 1:
   for i in range(count):
       nums_list.remove(False)

for i in nums_list:
    print(i)