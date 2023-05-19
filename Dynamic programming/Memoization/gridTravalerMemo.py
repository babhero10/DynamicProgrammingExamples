def grid_travaler(rows, cols):
	return grid_travaler_helper(rows, cols, {})

def grid_travaler_helper(rows, cols, memo):

	if (rows, cols) in memo:
		return memo[(rows, cols)]

	if (rows == 1 and cols == 1):
		return 1

	if (rows == 0 or cols == 0):
		return 0

	memo[(rows, cols)] = grid_travaler_helper(rows - 1, cols, memo) + grid_travaler_helper(rows, cols - 1, memo)

	return memo[(rows, cols)]

print(grid_travaler(1, 1))
print(grid_travaler(2, 3))
print(grid_travaler(3, 2))
print(grid_travaler(3, 3))
print(grid_travaler(18, 18))

