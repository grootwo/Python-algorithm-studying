# 9935
# 문자열 폭발

strings = input()
string_list = list(strings)
popping_string = input()

# 필요한 기능 pop, push, 확인
# 고민인데, 이걸 하나하나씩 확인하면 시간 초과이지 않을까?
# 그래도 해야지

popping_length = len(popping_string)

exists = True

print(strings, string_list, popping_string)

while exists:
    if len(string_list) < popping_length:
        break
    for i in range(0, len(string_list) - popping_length):
        if string_list[i:(i+popping_length)] == popping_string:
            print("exists")
    exists = False