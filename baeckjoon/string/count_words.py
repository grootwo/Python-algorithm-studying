# 1152

# 문장 입력받기
string = input()

# 문장 단어 개수 세기
count = 0
for i in range(len(string)):
    if string[i] != ' ':
        if (string[i - 1] == ' ') or (i == 0):
            count += 1

# 단어 개수 출력
print(count)

# # 공백제거
# 이걸로는 틀렸다고 함
# string = string.strip()
#
# # 문장 단어 개수 세기
# words = string.split(" ")
# words_count = len(words)
#
# # 단어 개수 출력
# print(words_count)