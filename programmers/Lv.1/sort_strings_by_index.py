# Lv.1
# 문자열 내 마음대로 정렬하기
def solution(strings, n):
    list_strings = [list(string) for string in strings]
    list_strings.sort(key=lambda x: (x[n], x)) # 인덱스, 사전순으로 단어 정렬
    strings = [''.join(list_str) for list_str in list_strings]
    return strings
