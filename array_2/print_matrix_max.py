# 2566
# 최댓값

matrix = []

for i in range(9):
	matrix.append(list(map(int, input().split())))

max = 0
max_x = 0
max_y = 0

for i in range(9):
	for j in range(9):
		if matrix[i][j] > max:
			max = matrix[i][j]
			max_x = i
			max_y = j

print(max)
print(max_x + 1, max_y + 1)