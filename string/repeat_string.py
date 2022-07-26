# 2675

# 케이스 개수 입력받기
num_line = int(input())

for i in range(num_line):
    # 반복횟수, 반복할 단어 입력받기
    num_word, word = input().split()

    # 반복해서 출력하기
    for j in range(len(word)):
        for k in range(int(num_word)):
            print(word[j], end="")
    print()

# ide마다 다른가 맞다고 뜸