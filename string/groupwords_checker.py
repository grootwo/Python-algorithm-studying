# 1316

num = int(input())
words = []
for i in range(num):
    words.append(input())

count = 0
def checker(string):
    length = len(string)
    check_dic = {}
    # for else문 이용 추천함
    for k in range(length):
        if string[k] not in check_dic:
           check_dic[string[k]] = 1
        else:
            if string[k - 1] == string[k]:
                continue
            else:
                return 0
    return 1


for j in range(num):
    if checker(words[j]) == 1:
        count += 1

print(count)