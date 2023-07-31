def solution(n, arr1, arr2):
    for i in range(5):
        arr1[i] = get_bi_str(arr1[i], n)
        arr2[i] = get_bi_str(arr2[i], n)
    result = [[0] * n for _ in range(n)]
    print(result)
    for i in range(5):
        for j in range(5):
            if arr1[i][j] == 0 and arr2[i][j] == 0:
                result[i][j] = ' '
            else:
                result[i][j] = '#'
    return result

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
