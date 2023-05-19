def grid_travaler(x, y):

	grid = [[0 for i in range(x+1)] for j in range(y+1)] 

	grid[1][1] = 1

	for i in range(0, y+1):
		for j in range(0, x+1):

			if i + 1 <= y:
				grid[i+1][j] += grid[i][j]

			if j + 1 <= x:
				grid[i][j+1] += grid[i][j]

	return grid[y][x]

print(grid_travaler(1, 1))
print(grid_travaler(2, 3))
print(grid_travaler(3, 2))
print(grid_travaler(3, 3))
print(grid_travaler(18, 18))