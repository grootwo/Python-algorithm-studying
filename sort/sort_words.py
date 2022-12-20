# 1181
# 단어 정렬
import sys

count = int(sys.stdin.readline())
words = []

for i in range(count):
    word = sys.stdin.readline().rstrip()
    words.append([word, len(word)])

words.sort(key=lambda x:(x[1], x[0]))

print(words[0][0])
for i in range(1, count):
    if words[i][0] != words[i - 1][0]:
        print(words[i][0])