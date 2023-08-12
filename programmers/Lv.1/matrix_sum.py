def solution(arr1, arr2):
    col = len(arr1[0])
    row = len(arr1)
    answer = [[0] * col for _ in range(row)]
    print(answer)
    for r in range(row):
        for c in range(col):
            answer[r][c] = arr1[r][c] + arr2[r][c]
    print(answer)
    return answer
