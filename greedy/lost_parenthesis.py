# 1541
# 잃어버린 괄호

string = input()

nums = []
signs = []
current = 0
for i in range(len(string)):
    if string[i] == '+' or string[i] == '-':
        nums.append(int(string[current:i]))
        signs.append(string[i])
        current = i + 1
    if i == len(string) - 1:
        nums.append(int(string[current:i + 1]))

result = nums[0]
minus = False
for j in range(1, len(nums)):
    if signs[j - 1] == '-':
        minus = True
    if minus == True # minus 나오는 순간 뒤의 수(절댓값) 다 빼주면 된다
        result -= nums[j]
    else:
        result += nums[j]

print(result)