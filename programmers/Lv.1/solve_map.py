def solution(n, arr1, arr2):
    for i in arr1:
        print(i, ':')
        print(get_bi_str(i, n))
    answer = []
    return answer

def get_bi_str(num, n):
    answer = ''
    temp = num
    while temp != 0:
        answer += str(temp % 2)
        temp = temp // 2
    left = n - len(answer)
    if left > 0:
        answer += '0' * left
    return answer[::-1]
