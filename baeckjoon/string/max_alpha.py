# 1157

# 단어 입력받기
word = input().upper()

# 각 글자별 글자 수 세기
count_dic = {}
for i in range(len(word)):
    char = word[i]
    if char not in count_dic:
        count_dic[char] = 1
    else:
        count_dic[char] += 1

word_dic = list(count_dic.keys())
num_dic = list(count_dic.values())

max_count = 0
for k in range(len(count_dic.keys())):
    if num_dic[k] > max_count:
        max_word = word_dic[k]
        max_count = num_dic[k]
    elif num_dic[k] == max_count:
        max_word = '?'

# 가장 빈도수가 높은 글자 출력
print(max_word)

# for i in range(len(word)):
#     char = word[i]
#     # 가장 빈도가 높은 글자 찾기
#     if word.count(char) > max_count:
#         max_count = word.count(char)
#         max_word = char
#     # 만약 최상 빈도수가 같은 글자가 있다면 ?로 대체
#     elif word.count(char) == max_count:
#         if max_word != char:
#             max_word = '?'