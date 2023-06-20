def solution(new_id):
    # 1
    new_id = list(new_id.lower())
    # 2
    allowed_symbols = ['-', '_', '.']
    remove_count = 0
    for i in range(len(new_id)):
        cha = new_id[i]
        cha_o = ord(cha)
        if cha_o < 48 or 57 < cha_o < 97 or 122 < cha_o:
            if cha not in allowed_symbols:
                new_id[i] = 0
                remove_count += 1
    for i in range(remove_count):
        new_id.remove(0)
    # 3
    answer = ''
    return answer
