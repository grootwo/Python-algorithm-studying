def solution(new_id):
    allowed_symbols = ['-', '_', '.']
    new_id = new_id.lower()
    for cha in new_id:
        cha_o = ord(cha)
        print(cha_o)
        if cha_o < 48 or 57 < cha_o < 97 or 122 < cha_o or cha_o not in allowed_symbols:
            print('no', cha)
    answer = ''
    return answer
