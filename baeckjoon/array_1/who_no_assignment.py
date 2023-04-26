# 5597
# 과제 안 내신 분..?

std_count = 28

std_list = []

for i in range(std_count):
    num = int(input())
    std_list.append(num)
std_list.sort()

for i in range(1, 31):
    if i not in std_list:
        print(i)