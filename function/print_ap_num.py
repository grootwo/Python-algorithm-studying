# 1065
# 한수

num = int(input())
count = 0

for i in range(1, num + 1):
    num_str = str(i)
    if len(num_str) == 1 or len(num_str) == 2:
        count += 1
    else:
        for j in range(1, len(num_str) + 1):
            