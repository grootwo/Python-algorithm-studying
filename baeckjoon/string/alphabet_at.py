# 10809

# 문자열 입력받기
string = str(input())

# 각각 알파벳이 문자열에서의 처음 위치 출력하기
for i in range(97, 123):
    word = chr(i)
    print(string.find(word), end=" ")