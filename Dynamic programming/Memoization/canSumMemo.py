def can_sum(number, list_of_numbers):
	return can_sum_helper(number, list_of_numbers, {})

def can_sum_helper(number, list_of_numbers, memo):

	if number in memo:
		return memo[number]

	if number == 0:
		return True

	if number < 0:
		return False

	for sub_value in list_of_numbers:

		sum_value = number - sub_value

		if can_sum_helper(sum_value, list_of_numbers, memo):
			memo[number] = True
			return True

	memo[number] = False
	return False

print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))