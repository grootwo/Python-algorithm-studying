def solution(food):
    food_table = []
    for i in range(len(food)):
        food[i] = food[i] // 2
    # print(food_table)
    # print(food)
    for i in range(1, len(food)):
        for j in range(food[i]):
            food_table.append(i)
    food_table.append(0)
    food.reverse()
    for i in range(len(food)):
        for j in range(food[i]):
            food_table.append(len(food) - 1 - i)
    # print(food_table)
    food_table = list(map(str, food_table))
    answer = ''.join(food_table)
    return answer
